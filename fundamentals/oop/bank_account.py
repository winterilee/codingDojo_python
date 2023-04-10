class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []

    def __init__(self, int_rate = 0.01, balance = 0): 
        # your code here! (remember, instance attributes go here)
        self.in_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # don't worry about user info here; we'll involve the User class soon
    
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        # your code here
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
    
    def display_account_info(self):
        # your code here
        print(f"Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        # your code here
        if BankAccount.check_positive(self.balance):
            self.balance += (self.balance * self.in_rate)
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
    
    @staticmethod
    def can_withdraw(balance, amount):
        if(balance - amount) < 0:
            return False
        else:
            return True
    
    @staticmethod
    def check_positive(balance):
        if balance < 0:
            return False
        else:
            return True
    
    @classmethod
    def list_all_accounts(cls):
        for account in cls.all_accounts:
            print(f"Balance: {account.balance}")


user_strawberry = BankAccount(balance = 700)
user_blueberry = BankAccount(0.02, 2000)

user_strawberry.deposit(100).deposit(50).deposit(200).withdraw(584).yield_interest().display_account_info()
user_blueberry.deposit(1200).deposit(800).withdraw(682).withdraw(312).withdraw(189).withdraw(1123).yield_interest().display_account_info()

BankAccount.list_all_accounts()