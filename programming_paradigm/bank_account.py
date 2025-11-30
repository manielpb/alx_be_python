class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        account_balance = 0
    
    def deposit(self,amount):
        self.account_balance += amount
    
    def withdraw(self,amount,account_balance):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            self.account_balance == account_balance

    def display_balance(self):
        return self.account_balance
