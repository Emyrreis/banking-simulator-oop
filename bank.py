from datetime import datetime

class Account:
    def __init__(self, agency, number, owner, password):
        self.agency = agency
        self.number = number
        self.owner = owner
        self.password = password
        self.balance = 0.0
        self.limit = -500.0
        self.pix_key = None
        self.transactions = []

    def check_password(self, pwd):
        return self.password == pwd

    def deposit(self, value, info="Depósito"):
        self.balance += value
        self.transactions.append((datetime.now(), info, value))

    def extrato(self):
        return self.transactions
