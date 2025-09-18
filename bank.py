from datetime import datetime

class Account:
    def __init__(self, name: str, agency: str, account_number: str, password: str, balance: float = 0.0, limit: float = -500.0):
        self.__name = name
        self.__agency = agency
        self.__account_number = account_number
        self.password = password
        self.__balance = balance
        self.__limit = limit
        self.pix_key = None
        self.__transactions = [] #Lista para guardar as transações 

    #Propriedades
    @property
    def name(self):
        return self.__name
    
    @property
    def agency(self):
        return self.__agency
    
    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def balance(self):
        return self.__balance
    
    @property
    def limit(self):
        return self.__limit
    
    #Métodos de verificação
    def check_password(self, pwd):
        return self.password == pwd
    
    def deposit(self, value: float):
        if value > 0:
            self.__balance += value
            self.__transactions.append(f"Depósito: +R$ {value:.2f}")
            return True
        return False
    
    def withdraw(self, value: float):
        if value > 0 and (self.__balance - value) >= self.__limit:
            self.__balance -= value
            self.__transactions.append(f"Saque: -R$ {value:.2f}")
            return True
        return False

    def extrato(self):
        return self.__transactions
