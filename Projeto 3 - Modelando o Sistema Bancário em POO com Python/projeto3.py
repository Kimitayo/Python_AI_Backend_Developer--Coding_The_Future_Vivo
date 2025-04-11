from abc import ABC, abstractmethod

# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)

# Pessoa Física herda de Cliente
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @staticmethod
    def verificar_usuario(cpf, clientes):
        return any(cliente._cpf == cpf for cliente in clientes)

    @staticmethod
    def criar_cliente(cpf, nome, data_nascimento, endereco, clientes):
        if not PessoaFisica.verificar_usuario(cpf, clientes):
            novo_cliente = PessoaFisica(cpf, nome, data_nascimento, endereco)
            clientes.append(novo_cliente)
            print(f"Usuário criado com sucesso!")
            return novo_cliente
        else:
            print("Cliente já existente.")
            return None

# Classe Conta
class Conta:
    def __init__(self, saldo, numero, agencia, cliente):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente

    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        print("Saldo insuficiente.")
        return False

    def deposito(self, valor):
        if valor >= 0:
            self._saldo += valor
            return True
        print("Valor inválido.")
        return False

# Classe Abstrata Transação
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

# Depósito
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.deposito(self.valor)
        print(f"\nDepósito de R${self.valor:.2f} realizado com sucesso.")

# Saque
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)
        print(f"\nSaque de R${self.valor:.2f} realizado com sucesso.")

# Conta Corrente
class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, limite=500, limite_saques=3):
        super().__init__(saldo, numero, agencia, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._numero_saques = 0

    def sacar(self, valor):
        if valor > self._limite:
            print("Valor de saque excede o limite permitido.")
            return False
        elif self._numero_saques >= self._limite_saques:
            print("Você atingiu o limite de saques diários.")
            return False
        elif super().sacar(valor):
            self._numero_saques += 1
            return True
        return False

# Histórico
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, transacao, conta):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "saldo_apos": conta.saldo()
        })

    def mostrar(self):
        print("\n================ Extrato ================")
        if not self.transacoes:
            print("Nenhuma transação realizada.")
        for t in self.transacoes:
            print(f"{t['tipo']}: R${t['valor']:.2f} | Saldo após: R${t['saldo_apos']:.2f}")
        print("==========================================\n")

# MAIN
clientes = []
contas = []
historico = Historico()

print("Olá, caro cliente.")
menu_inicial = input("Já é cliente? [1] Sim [2] Não: ")

if menu_inicial == "1":
    cpf = input("Digite seu CPF: ")
    cliente_encontrado = next((c for c in clientes if c._cpf == cpf), None)
    if cliente_encontrado:
        cliente = cliente_encontrado
    else:
        print("Cliente não encontrado.")
        exit()

else:
    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereço: ")

    cliente = PessoaFisica.criar_cliente(cpf, nome, data_nascimento, endereco, clientes)
    if cliente is None:
        exit()

# Criação da conta
numero = len(contas) + 1
conta1 = ContaCorrente(0, numero, "0001", cliente)
cliente.adicionar_conta(conta1)
contas.append(conta1)

# MAIN
while True:
    opcao = input(f"""
----------------------------------------------
              Banco Brasileiro

Olá, {cliente._nome}. O que você deseja fazer?

[1] Depositar
[2] Sacar
[3] Extrato
[4] Adicionar nova conta
[5] Sair

Escolha uma opção => """)

    if opcao == "1":
        valor = float(input("Digite o valor de depósito: R$"))
        transacao = Deposito(valor)
        transacao.registrar(conta1)
        historico.adicionar(transacao, conta1)

    elif opcao == "2":
        valor = float(input("Digite o valor de saque: R$"))
        transacao = Saque(valor)
        transacao.registrar(conta1)
        historico.adicionar(transacao, conta1)

    elif opcao == "3":
        historico.mostrar()

    elif opcao == "5":
        print("Obrigado por usar o Banco Brasileiro!")
        break

    elif opcao == "4":
        numero = len(contas) + 1
        nova_conta = ContaCorrente(0, numero, "0001", cliente)
        cliente.adicionar_conta(nova_conta)
        contas.append(nova_conta)
        conta1 = nova_conta 
        print(f"Nova conta adicionada com sucesso! Número: {numero}")

    else:
        print("Opção inválida.")
