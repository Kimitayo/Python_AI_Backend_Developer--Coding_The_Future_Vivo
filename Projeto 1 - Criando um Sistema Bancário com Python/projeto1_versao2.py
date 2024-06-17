menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação inválida!")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

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

    elif opcao == "e":
        extrato += f"Saldo = R$ {saldo:.2f}\n"
        print(f"{extrato}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
