class BankAccount:
    def __init__(self, name, account_number, account_balance):
        self.name = name
        self.account_number = account_number
        self.account_balance = account_balance

    def account_informations(self):
        return {"name": self.name, 
              "account_number": self.account_number,
              "account_balance": self.account_balance}

    def withdraw(self, value):
        self.account_balance -= value

    def deposit(self, value):
        pass


