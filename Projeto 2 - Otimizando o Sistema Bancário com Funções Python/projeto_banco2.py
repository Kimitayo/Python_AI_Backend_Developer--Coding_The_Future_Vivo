def saque(saldo, valor, extrato, numero_saques, LIMITE_SAQUES): #keywords only (saldo=saldo, valor=valor,...)
    if (valor<=saldo and valor<=500 and numero_saques<=LIMITE_SAQUES):
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
    elif valor>saldo:
            print("Saldo insuficiente!")
    elif valor>500:
            print("Valor limitado a R$ 500,00 por saque!")
    elif numero_saques>LIMITE_SAQUES:
            print("Limite de saques foi atingido!")

    return saldo, extrato, numero_saques


def deposito(saldo, valor, extrato): #positional only
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação inválida!")

    return saldo, extrato

def mostrar_extrato(extrato, /, saldo): #keywords and positional
    extrato += f"Saldo = R$ {saldo:.2f}\n"
    print(f"{extrato}")

    return extrato

# Função de verificar a existencia de cliente
def verificar_usuario(cpf):
    def cpf_do_usuario(usuario):
        return usuario['cpf'] == cpf
    
    cpf_filtrado = filter(cpf_do_usuario, usuarios)
    cpf_filtrado = list(cpf_filtrado)

    if cpf_filtrado == []:
        return False

    else:
        return True

# Funções dos clientes
def criar_usuario(nome, data_nascimento, cpf, endereco):
    def cpf_do_usuario(usuario):
        return usuario['cpf'] == cpf
    
    cpf_filtrado = filter(cpf_do_usuario, usuarios)
    cpf_filtrado = list(cpf_filtrado)

    if cpf_filtrado == []:
        usuario = { #dicionário
          "nome": nome,
          "dataNascimento": data_nascimento,
          "cpf": cpf,
          "endereco": endereco #rua, numero - bairro - cidade/sigla
        }
        usuarios.append(usuario)
        numero_da_conta = 0;
        print("Usuário criado com sucesso!\nNúmero da conta = ", numero_da_conta, "\nAgência = 0001") 

    else:
        print("Cliente já existente!") 
    

def criar_conta(numero_da_conta, usuario, AGENCIA = "0001"):
    conta = {
        AGENCIA: "0001",
        'numero_da_conta': numero_da_conta,
        'usuario': usuario
    }
    contas.append(conta)
                
    print("Agência: ", AGENCIA, "\nNúmero da conta: ", numero_da_conta)
    
    


#Lista de usuários
contas = []
usuarios = []

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_da_conta = 0

menu_inicial2 = False

menu_inicial1 = input(f"""
----------------------------------------------
              Banco Brasileiro

Olá, caro cliente. Já é cliente?

[1] Sim
[2] Não

Escolha uma opção => """)


if menu_inicial1 == "1":
    nome = input("Digite seu nome => ")
    #data_nascimento = input("Digite sua data de nascimento => ")
    cpf = input("Digite seu cpf => ")
    #endereco = input("Digite seu endereço => ")
    
    verificar_usuario(cpf)
    if (verificar_usuario == True):
         menu_inicial2 = True
    else:
        print("Usuário não encontrado!")
        menu_inicial1 = input("Deseja se cadastrar? Digite '1' para Sim e '2' para não => ")

        if (menu_inicial1 == '1'):
            data_nascimento = input("Digite sua data de nascimento => ")
            endereco = input("Digite seu endereço => ")
            criar_usuario(nome, data_nascimento, cpf, endereco)
            numero_da_conta = 0
            menu_inicial2 = True
        else:
            print("Sua operação está encerrada!")

else:
    menu_inicial1 =  input("Deseja se cadastrar? Digite '1' para Sim e '2' para não => ")
    if (menu_inicial1 == '1'):
        nome = input("Digite seu nome => ")
        data_nascimento = input("Digite sua data de nascimento => ")
        cpf = input("Digite seu cpf => ")
        endereco = input("Digite seu endereço => ")

        criar_usuario(nome, data_nascimento, cpf, endereco)
        numero_da_conta = 0
        menu_inicial2 = True

        print("")
    else:
        print("Sua operação está encerrada!")




while (menu_inicial2 == True):
    menu_opcoes1 = input(f"""
----------------------------------------------
              Banco Brasileiro

Olá, {nome}. O que você deseja fazer hoje?

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar outra conta
[5] Sair

Escolha uma opção => """)
         
    if menu_opcoes1 == "1":
        valor = float(input("Informe o valor do depósito: "))
        print(deposito(saldo=saldo, valor=valor, extrato= extrato))
        saldo, extrato = deposito(saldo, valor, extrato)
                
        
    elif menu_opcoes1 == "2":
        valor = float(input("Informe o valor de saque: "))
        print(saque(saldo, valor, extrato, numero_saques, LIMITE_SAQUES))
        saldo, extrato, numero_saques = saque(saldo, valor, extrato, numero_saques, LIMITE_SAQUES)
            
    elif menu_opcoes1 == "3":
        print(mostrar_extrato(extrato, saldo=saldo))
        
    elif menu_opcoes1 == "4":
        for usuario in usuarios:
            if usuario['cpf'] == cpf:
                numero_da_conta = numero_da_conta+1
                criar_conta(numero_da_conta, usuario, AGENCIA = "0001")

    elif menu_opcoes1 == "5":
         print("Obrigada por usar!")
         menu_inicial2 = False

"""
for usuario in usuarios:
    if usuario['nome'] == 'Alice':
        # Adicionando um dicionário de contatos
        usuario['contatos'] = {
            'email': 'alice@example.com',
            'telefone': '1234-5678'
        }
"""
        
