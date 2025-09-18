from bank import Account

#Testando
conta = Account("Emilly Reis", "0001", "12345-6", "1234", balance = 1000.0)

while True:
    print("APP Bank")
    senha = input("Digite sua senha: ")
    if conta.check_password(senha):
        while True:
            print(f"Bem Vindo(a) {conta.name}")
            print("1 - Depositar")
            print("2 - Sacar")
            print("3 - Ver extrato")
            print("4 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                valor = float(input("Digite o valor do depósito: "))
                if conta.deposit(valor):
                    print("Depósito realizado com sucesso!")
                else:
                    print("Valor inválido.")
            
            elif opcao == "2":
                valor = float(input("Digite o valor do saque: "))
                if conta.withdraw(valor):
                    print("Saque realizado com sucesso!")
                else:
                    print("Saque não permitido (saldo insuficiente).")
            
            elif opcao == "3":
                print("Extrato:")
                for t in conta.extrato():
                    print("-", t)
                print(f"Saldo atual: R$ {conta.balance:.2f}")
            
            elif opcao == "4":
                print("Saindo...")
                break

            else:
                print("Opção inválida.")
    else:
        print("Senha inválida")


