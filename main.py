from bank import Account

#Testando
conta1 = Account("Emilly Reis", "0001", "12345-6", "1234", balance = 1000.0)
conta2 = Account("Bella Santos", "0002", "67891-1", "4321", balance = 500.0)

#conta2.create_pix_key(123456789)

while True:
    print("\nAPP Bank")
    senha = input("Digite sua senha: ")
    if conta1.check_password(senha):
        print(f"\nNome: {conta1.name}")
        print(f"Conta: {conta1.account_number}")
        print(f"Agência: {conta1.agency}")
        print(f"Saldo: {conta1.balance}")

        while True:
            print(f"\nBem Vindo(a) {conta1.name}")
            print("1 - Depositar")
            print("2 - Sacar")
            print("3 - Ver extrato")
            print("4 - Criar chave Pix")
            print("5 - Enviar Pix")
            print("6 - Alterar limite")
            print("7 - Alterar senha")
            print("8 - Sair")

            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                valor = float(input("Digite o valor do depósito: "))
                if conta1.deposit(valor):
                    print("Depósito realizado com sucesso!")
                    print(f"Saldo atual: R${conta1.balance:.2f}")
                else:
                    print("Valor inválido.")

            elif opcao == "2":
                valor = float(input("Digite o valor do saque: "))
                if conta1.withdraw(valor):
                    print("Saque realizado com sucesso!")
                    print(f"Saldo atual: R${conta1.balance:.2f}")
                else:
                    print("Saque não permitido (valor inválido ou saldo insuficiente).")

            elif opcao == "3":
                print("Extrato: ")
                for t in conta1.extrato():
                    print("-", t)
                print(f"\n- Saldo atual: R${conta1.balance:.2f}")

            elif opcao == "4":
                chave = input("Digite a chave Pix para cadastrar: ")
                if conta1.create_pix_key(chave):
                    print("Chave Pix cadastrada com sucesso!")
                else:
                    print(f"Você já possui uma chave Pix cadastrada: {conta1.pix_key}")

            elif opcao == "5":
                valor = float(input("Digite o valor do Pix: "))
                keyp = input("Digite a chave Pix: ")
                destination = conta1.send_pix(valor, keyp, conta1, conta2)
                if destination:
                    print(f"Pix de R${valor:.2f} enviado com sucesso para {destination.name}!")
                else:
                    print("Erro ao enviar Pix (verifique saldo ou chave do destino).")

            elif opcao == "6":
                print(f"Limite atual: R$ {conta1.limit:.2f}")
                novo_limite = float(input("Digite o novo limite: "))
                conta1.change_limit(novo_limite)
                print(f"Limite alterado para R${novo_limite:.2f} com sucesso!")

            elif opcao == "7":
                antiga = input("Digite sua senha atual: ")
                nova = input("Digite a nova senha: ")
                if conta1.change_password(antiga, nova):
                    print("Senha alterada com sucesso. Faça login novamente.")
                    break 
                else:
                    print("Senha atual incorreta.")

            elif opcao == "8":
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

    else:
        print("Senha inválida! Tente novamente.\n")