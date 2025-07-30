class BankAccount:
    """This Class interfaces with main.py to use command line inputs in order to perfor banking operations"""
    def __init__(self, account_balance = 0 ):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        if self.account_balance >= amount:
            return True
        else :
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
    
    
        