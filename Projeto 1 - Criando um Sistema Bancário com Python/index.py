"""
# DESAFIO

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: *depósito, saque e extrato*.

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os *depósitos devem ser armazenados em uma variável* e *exibidos na operação de extrato*.

O sistema deve permitir realizar *3 saques diários* com *limite máximo de R$ 500,00 por saque*. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os *saques devem ser armazenados em uma variável* e *exibidos na operação de extrato*.



# OPERAÇÕES DE EXTRATO
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser *exibido o saldo atual da conta*. Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

"""

import textwrap

# MENUS
def menu_inicial():
    menu = """
--------- BANCO BRASILEIRO ---------
  Bem vindo(a) ao Banco Brasileiro!

(1) Entrar
(2) Cadastrar
(3) Sair

=> """
    return input(textwrap.dedent(menu))

def login(usuarios):
    cpf = input("Insira seu cpf => ")
    nome = None

    if filtrar_usuario(cpf, usuarios) is True:
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                nome = usuario["nome"]
        return nome
    else:
        print("\nVocê não está cadastrado!")
        return False

def menu_entrar(nome):
    menu = f"""
Olá, {nome}! O que você gostaria de fazer?

(1) Depósito
(2) Saque
(3) Extrato 
(4) Sair

=> """
    return input(textwrap.dedent(menu))

# CRIAR USUÁRIO
def criar_usuario(usuarios):
    usuario = {}

    print("Você selecionou a opção cadastrar!\n")
    usuario["cpf"] = input("Informe o número de seu CPF => ")

    if filtrar_usuario(usuario["cpf"], usuarios) is True:
        print("\nUm cadastro com esse cpf já foi realizado\n")
        return

    nome = input("Informe o seu nome completo => ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa) => ")
    endereco = input("Informe o seu endereço completo (rua, nro - bairro - cidade/sigla estado) => ")

    usuario["nome"] = nome
    usuario["data_nascimento"] = data_nascimento
    usuario["endereco"] = endereco
    
    usuarios.append(usuario)

    print("\nUsuário criado com sucesso!\n")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return True
    return None

# OPERAÇÕES
def deposito(saldo):
    deposito_valor = float(input("Insira o valor de depósito => "))

    if deposito_valor >= 0:
        saldo += deposito_valor
        print(f"O seu novo saldo é R$ {saldo: .2f}")
        return saldo, deposito_valor
    else:
        print("Valor negado")
        return saldo, None

def saque(saldo, qunt_saque):
    saque_valor = float(input("Insira o valor de saque => "))

    if saque_valor <= 500:
        if saque_valor >= 0 and saque_valor <= saldo and qunt_saque < 3:
            saldo -= saque_valor
            qunt_saque += 1
            print(f"O novo saldo é R$ {saldo: .2f}")
            return saldo, qunt_saque, saque_valor
        elif saque_valor >= 0 and saque_valor <= saldo and qunt_saque >= 3:
            print("Limite de saques excedido")
            return saldo, qunt_saque, None
        elif saldo == 0 and qunt_saque < 3:
            print("Não é possível sacar dinheiro por falta de saldo")
            return saldo, qunt_saque, None
        else:
            print("Valor negado")
            return saldo, qunt_saque, None
    else:
        print("Valor de saque acima do permitido")
        return saldo, qunt_saque, None

def extrato_ex():
    texto_extrato = """
--------- BANCO BRASILEIRO ---------
              EXTRATO"""
    return print(textwrap.dedent(texto_extrato))

# MAIN
def main():
    usuarios = []
    saldo_novo = 0.0
    qunt_saque = 0
    extrato = []

    while True:
        opcao_menu_inicial = menu_inicial()

        if opcao_menu_inicial == "2":
            criar_usuario(usuarios)
        elif opcao_menu_inicial == "1":

            nome_resgatado = login(usuarios)
            if nome_resgatado is not False:

                while True:
                    opcao = menu_entrar(nome_resgatado)
    
                    match opcao:
                        case "1":
                            saldo_novo, deposito_valor = deposito(saldo_novo)
                            if deposito_valor is not None:
                                extrato.append(f"\nDepósito de R$ {deposito_valor}\nSaldo de R$ {saldo_novo}")
                        case "2":
                            saldo_novo, qunt_saque, saque_valor = saque(saldo_novo, qunt_saque)
                            if saque_valor is not None:
                             extrato.append(f"\nSaque de R$ {saque_valor}\nSaldo de R$ {saldo_novo}")
                        case "3":
                            extrato_ex()
                            for transacao in extrato:
                                print(transacao)
                            print(f"""------------------------------------""")
                        case "4":
                            print("Obrigado por usar o nosso banco!")
                            break
                        case _:
                            print("/n!!! ERRO: Opção inválida. Tente novamente. !!!\n")
        else:
            print("Finalizando sessão")
            break

main()