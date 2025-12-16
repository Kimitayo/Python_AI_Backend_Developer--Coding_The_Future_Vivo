import textwrap
from abc import ABC, abstractmethod

# Cliente (Mãe)
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta): 
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

# Pessoa Física (filha de cliente)
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# Conta (Mãe)
class Conta():
    def __init__(self, numero, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def depositar(self, valor:float):
        if  valor > 0:
            self.saldo += valor
            print(f"O seu novo saldo é de R$ {self.saldo: .2f}")
            return True
        else: 
            print("Valor negado")
            return False
        
    def sacar(self, valor:float):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"O seu novo saldo é {self.saldo: .2f}")
            return True
        else: 
            return False
        
    def exibir_extrato(self):
        print(f"\n=== EXTRATO DA CONTA Nº {self.numero} ===")
        if not self.historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self.historico.transacoes:
                print(f"{transacao.__class__.__name__}:\tR$ {transacao.valor:.2f}")

        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")

# Conta Corrente (filha de conta)
class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)
        self.limite = 500
        self.limite_saques = 3
        self.num_saques = 0

    def sacar(self, valor):
        if valor <= self.limite:
            if valor > 0 and valor <= self.saldo and self.num_saques < self.limite_saques:
                self.saldo -= valor
                self.num_saques += 1
                print(f"O novo saldo é R$ {self.saldo: .2f}")
                return True
            elif valor > 0 and valor <= self.saldo and self.num_saques >= self.limite_saques:
                print("Limite de saques excedido")
                return False
            elif self.saldo == 0 and self.num_saques < self.limite_saques:
                print("Não é possível sacar por falta de saldo")
                return False
            else:
                print("Valor negado")
                return False
        else:
            print("Valor de saque acima do permitido")
            return False

# Historico
class Historico():
    def __init__(self):
        self.transacoes= []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

# Interface Transacao
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

# Depósito (filha de transacao)
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            print("Depósito registrado com sucesso.")
            return True
        
        print("Falha ao registrar depósito.")
        return False
    
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
            print("Saque registrado com sucesso.")
            return True
        
        print("Falha ao registrar saque.")
        return False
    
# Filtrar Usuário
def filtrar_usuario(usuarios, cpf):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None

def escolher_conta(cliente):
    if not cliente.contas:
        print("Cliente não possui contas.")
        return None
    
    if len(cliente.contas) == 1:
        return cliente.contas[0]

    print("\n--- SELEÇÃO DE CONTA ---")
    print(f"O cliente {cliente.nome} possui várias contas.")
    for i, conta in enumerate(cliente.contas):

        print(f"{i+1} - Conta Nº: {conta.numero} (Saldo: {conta.saldo:.2f})")


    try:
        opcao = int(input("Escolha o número da conta para operar => "))
        return cliente.contas[opcao - 1]
    except (ValueError, IndexError):
        print("Opção inválida! Selecionando a primeira conta por padrão.")
        return cliente.contas[0]


# CRIAR USUÁRIO
def criar_usuario(usuarios):
    print("--- CADASTRAR NOVO USUÁRIO ---")

    cpf = input("Insira seu CPF => ")
    
    if filtrar_usuario(usuarios, cpf) is not None:
        print("Um cadastro com esse CPF já foi realizado")
        return
    
    nome = input("Insira seu nome completo => ")
    data_nascimento = input("Insira a sua data de nascimento => ")
    endereco = input("Insira seu endereço => ")

    novo_cliente_objeto = PessoaFisica(nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco)
    usuarios.append(novo_cliente_objeto)
    print(f"Usuário '{nome}' criado com sucesso!")

# CRIAR CONTA
def criar_conta(contas, usuarios):
    print("--- CRIAÇÃO DE NOVA CONTA ---")

    cpf = input("Digite novamente o seu CPF => ")
    usuario_encontrado = filtrar_usuario(usuarios, cpf)

    if usuario_encontrado is None:
        print("Cliente não encontrado")
        return
    
    numero_nova_conta = len(contas)+1

    nova_conta = ContaCorrente(numero=numero_nova_conta, cliente=usuario_encontrado)

    contas.append(nova_conta)
    usuario_encontrado.adicionar_conta(nova_conta)

    print(f"\nConta Corrente nº {numero_nova_conta} criada com sucesso para o cliente '{usuario_encontrado.nome}'!")
        

# MENUS
def menu_inicial():
    menu = """
--------- BANCO BRASILEIRO ---------
  Bem vindo(a) ao Banco Brasileiro!

(1) Entrar
(2) Cadastrar
(3) Criar Nova Conta
(4) Sair

=> """
    return input(textwrap.dedent(menu))

def menu_entrar(conta):

    menu = f"""
--- CONTA ATIVA: {conta.numero} ---
O que você gostaria de fazer?

(1) Depósito
(2) Saque
(3) Extrato 
(4) Voltar / Sair da conta

=> """
    return input(textwrap.dedent(menu))

# MENU
def main():
    usuarios = []
    contas = []

    while True:
        opcao_menu_inicial = menu_inicial()

        if opcao_menu_inicial == "2":
            criar_usuario(usuarios)
            criar_conta(contas, usuarios) 

        elif opcao_menu_inicial == "1":
            cpf = input("Digite seu CPF => ")
            usuario_encontrado = filtrar_usuario(usuarios, cpf)

            if usuario_encontrado is None:
                print("Usuário não encontrado, por favor tente novamente.")
                continue
            
            if not usuario_encontrado.contas:
                print("Usuário não possui conta cadastrada.")
                continue


            conta_selecionada = escolher_conta(usuario_encontrado)
            
            if conta_selecionada is None:
                 continue 

            while True: 
                opcao = menu_entrar(conta_selecionada) 

                match opcao:
                    case "1":
                        valor = float(input("Insira o valor do depósito => "))
                        deposito = Deposito(valor)
  
                        deposito.registrar(conta_selecionada)

                    case "2":
                        valor = float(input("Insira o valor do saque => "))
                        saque = Saque(valor)
  
                        saque.registrar(conta_selecionada)

                    case "3":
    
                        conta_selecionada.exibir_extrato()

                    case "4":
                        print("Saindo da conta...")
                        break 
                    
                    case _:
                        print("Opção inválida.")

        elif opcao_menu_inicial == "3":
            criar_conta(contas, usuarios)

        elif opcao_menu_inicial == "4":
            print("Finalizando sessão")
            break

        else:
            print("Opção inválida.")

main()