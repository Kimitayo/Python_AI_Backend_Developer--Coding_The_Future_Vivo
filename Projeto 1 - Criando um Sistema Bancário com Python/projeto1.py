nome = input("Digite o seu nome: ")


saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3
novo_deposito_validacao = True
programa = True


while(programa==True):
    menu = input(f"""
    ----------------------------------------------
                  Banco Brasileiro

    Olá, {nome}. O que você deseja fazer hoje?

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair

    Escolha uma opção: """)
        

    # Depositar
    if (menu == "1"):
        print("\nVocê escolheu a opção 1.")

        while (novo_deposito_validacao == True):
            saldo_adicionado = float(input("Digite o valor que gostaria de depositar: "))

            if (saldo_adicionado > 0):
                saldo += saldo_adicionado
                
                novo_deposito = input("""\nDepósito realizado com sucesso!
                                        Gostaria de fazer um novo depósito?
                                        SIM  Digite 'sim' pra depositar um outro valor
                                        NÃO  Digite 'não' para encerrar o programa
                                        => """)
                if novo_deposito.lower() == "não":
                    break
                    

            else:
                novo_deposito = input(f"""Valor de depósito não reconhecido! Gostaria de digitar um outro valor para depósito? 
                                        SIM  Digite 'sim' para depositar um outro valor
                                        NÃO  Digite 'não' para encerrar a operação
                                        => """)
                if novo_deposito.lower() == "não":
                    break
          
            
        
    # Sacar
    if (menu=="2"):
        print("\nVocê escolheu a opção 2.")

        while (numero_saques <= LIMITE_SAQUES):
            valor_de_saque = float(input("Digite o valor que gostaria de sacar: "))

            if (valor_de_saque <= saldo and valor_de_saque>0):
                saldo -= valor_de_saque
                numero_saques += 1
                continuar_saque = input("""Saque realizado com sucesso!
                                        Gostaria de fazer um novo saque?
                                        SIM  Digite 'sim' pra sacar um outro valor
                                        NÃO  Digite 'não' pra voltar ao menu inicial
                                        => """)

                if (continuar_saque.lower() == "não"):
                    break
            else:
                continuar_saque = input(f"""Valor de saque inferior ao saldo! Gostaria de digitar um outro valor para saque? 
                                            SIM  Digite 'sim' para sacar um outro valor
                                            NÃO  Digite 'não' para encerrar a operação
                                            => """)
                if (continuar_saque.lower() == "sim"):
                    numero_saques = 0
                

            # Saque acima de 500
            if (valor_de_saque > 500):
                continuar_saque = input(f"""Limite de R$ 500,00 por saque! Gostaria de digitar um outro valor para saque? 
                                            SIM  Digite 'sim' para sacar um outro valor
                                            NÃO  Digite 'não' para encerrar a operação
                                            => """)
                if (continuar_saque.lower() == "sim"):
                    numero_saques = 0
                else:
                    break


    # Extrato
    if (menu=="3"):
        print(f"""
        ===============EXTRATO===============
        Cliente: {nome}
        Saldo: R$ {saldo}

        =====================================

""")
        
    
    # Sair
    if (menu=="4"):
        print("""
                          
                          
              Obrigado por usar!

              ------FIM DO PROGRAMA------
                          
            """)
        programa=False
            


