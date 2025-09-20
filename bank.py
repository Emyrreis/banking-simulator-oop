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
    
    def change_password(self, old_pwd, new_pwd):
        if self.check_password(old_pwd):
            self.password = new_pwd
            return True
        return False
    
    def deposit(self, value: float):
        if value > 0:
            self.__balance += value
            self.__transactions.append(f"{datetime.now()} | Depósito: +R${value:.2f}")
            return True
        return False
    
    def withdraw(self, value: float):
        if value > 0 and (self.__balance - value) >= self.__limit:
            self.__balance -= value
            self.__transactions.append(f"{datetime.now()} | Saque: -R${value:.2f}")
            return True
        return False

    def extrato(self):
        return self.__transactions
    
    #Métodos do pix
    def create_pix_key(self, key: str):
        if not self.pix_key:
            self.pix_key = key
            return True
        return False
    
    def send_pix(self, value: float, destination_key: str, conta1, conta2):
        if value <= 0:
            return False

        if (self.balance - value) < self.limit:
            return False

        destination_account = None
        for c in (conta1, conta2):
            if str(c.pix_key) == str(destination_key):
                destination_account = c
                break

        if not destination_account:
            return False

        self._Account__balance -= value
        destination_account._Account__balance += value

        # Registra no extrato junto com as movimentações do saque e depósito
        self._Account__transactions.append(f"{datetime.now()} | Pix enviado: -R${value:.2f} para {destination_account.name}")
        destination_account._Account__transactions.append(f"{datetime.now()} | Pix recebido: +R${value:.2f} de {self.name}")

        return True

    #Método do limite
    def change_limit(self, new_limit: float):
        self.__limit = new_limit
        self.__transactions.append(f"{datetime.now()} | Alteração de limite: R${new_limit:.2f}")
        return True
