menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
          print("Opção selecionada inválida. Escolha uma nova opção!")
           
    elif opcao == "2":
        valor_saque = float(input("Digite o valor que deseja sacar: "))

        if valor_saque > limite:
            print("Valor de saque não permitido, pois excedeu o valor permitido.")

        elif valor_saque > saldo:
            print("Saldo insuficiente.")

        elif numero_saques >= LIMITE_SAQUES:
            print("limite diário de saques foi excedido.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"\nSaque: R$ {valor_saque:.2f}"
            numero_saques += 1

        else:
            print("Valor informado inválido.")

    elif opcao == "3":
        print("\n===========================Extrato===========================")
        print("Não houve nenhuma movimentação" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================================================")

        
    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
