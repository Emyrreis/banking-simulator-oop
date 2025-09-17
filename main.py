from bank import Account

conta = Account("0001", "12345-6", "Emilly", "1234")

print("Simulador Bancário")
senha = input("Digite sua senha: ")

if conta.check_password(senha):
    print(f"\nBem-vinda, {conta.owner}!")
    conta.deposit(1000, "Depósito inicial")
    print(f"Agência: {conta.agency} | Conta: {conta.number}")
    print(f"Saldo atual: R$ {conta.balance:.2f}")
else:
    print("Senha incorreta.")
