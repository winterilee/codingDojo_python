# class BankAccount:
#     # Declaring a class attribute
#     # Shared among all bank accounts
#     bank_name = "First National Dojo"		
    
#     def __init__(self, int_rate, balance):
#         self.int_rate = int_rate
#         self.balance = balance

# adriensAccount = BankAccount(0.02, 500)
# sadiesAccount = BankAccount(0.03, 100)
# adriensAccount.bank_name = "Dojo Credit Union"
    
# print(adriensAccount.bank_name)
# # output: Dojo Credit Union
    
# print(sadiesAccount.bank_name)
# # output: First National Dojo

# BankAccount.bank_name = "Bank of Dojo"
    
# print(adriensAccount.bank_name)
# # output: Bank of Dojo
    
# print(sadiesAccount.bank_name)
# # output: Bank of Dojo

class BankAccount:
    # class attributes
    bank_name = "First National Dojo"
    # new class attribute - a list of all the accounts!
    all_accounts = []
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    def with_draw(self,amount):
        # we can use the static method here to evaluate
        # if we can with draw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum
    
        # static methods have no access to any attribute
    # only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True


mochi_account = BankAccount(0.02, 500)
cookie_account = BankAccount(0.03, 1000)

mochi_account.bank_name = "Dojo National"
print(mochi_account.bank_name)
print(cookie_account.bank_name)

BankAccount.bank_name = "Bank of Dojo"
print(mochi_account.bank_name)
print(cookie_account.bank_name)

print(BankAccount.all_balances())

print(cookie_account.balance)
cookie_account.with_draw(800)
print(cookie_account.balance)
cookie_account.with_draw(500)

