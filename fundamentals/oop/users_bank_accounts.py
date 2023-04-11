class BankAccount:
    all_accounts = []

    def __init__(self, int_rate = 0.02, balance = 0): 
        self.in_rate = int_rate
        self.balance = balance
        self.savings_balance = None
        BankAccount.all_accounts.append(self)
    
    def deposit_checking(self, amount):
        self.balance += amount
        return self
    
    def deposit_savings(self, amount):
        if self.savings_balance == None:
            print("User does not have any Savings Account.")
        else:
            self.savings_balance += amount
        return self
    
    def withdraw_checking(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def withdraw_savings(self, amount):
        if self.savings_balance == None:
            print("User does not have any Savings Account.")
        else:
            if BankAccount.can_withdraw(self.savings_balance, amount):
                self.savings_balance -= amount
            else:
                print("Insufficient funds: Charging a $5 fee")
                self.savings_balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Checking Balance: ${self.balance} \n Savings Balance: ${self.savings_balance}")
        return self
    
    def yield_interest_checking(self):
        if BankAccount.check_positive(self.balance):
            self.balance += (self.balance * self.in_rate)
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def yield_interest_savings(self):
        if self.savings_balance == None:
            print("User does not have any Savings Account.")
        else:
            if BankAccount.check_positive(self.savings_balance):
                self.savings_balance += (self.savings_balance * self.in_rate)
            else:
                print("Insufficient funds: Charging a $5 fee")
                self.savings_balance -= 5
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


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)
    
    # other methods
    
    def make_deposit(self, amount):
        # your code here
        check_accounts = input(f"{self.name}, you are making a deposit: ${amount}, Checking or Savings? (C/S) \n")
        if check_accounts == "C":
            self.account.deposit_checking(amount)
        elif check_accounts == "S":
            self.account.deposit_savings(amount)
        else:
            print("Incorrect command. Please try again.")
        return self
    
    def make_withdrawal(self, amount):
        check_accounts = input(f"{self.name}, you are making a withdrawal: ${amount}, Checking or Savings? (C/S) \n")
        if check_accounts == "C":
            self.account.withdraw_checking(amount)
        elif check_accounts == "S":
            self.account.withdraw_savings(amount)
        else:
            print("Incorrect command. Please try again.")
        return self
    
    def display_user_balance(self):
        print("-" * 40)
        print(f"User: {self.name}, Checking Balance: ${self.account.balance} \nUser: {self.name}, Savings Balance: ${self.account.savings_balance}")
        print("-" * 40)
        return self
    
    def open_savings_account(self, amount = 0):
        if self.account.savings_balance == None:
            self.account.savings_balance = amount
            print(f"{self.name}, you have successfully opened your Savings Account.")
        else:
            print(f"{self.name}, you already have a Savings Account.")
        return self
    
    def transfer_money(self, amount, other_user):
        check_self_account = input(f"{self.name}, you are about to send ${amount} to {other_user.name}. Please choose your account: Checking or Savings? (C/S) \n")
        check_other_account = input(f"{self.name}, please choose {other_user.name}'s account: Checking or Savings? (C/S) \n")
        if check_self_account == "C":
            self.account.balance -= amount
        elif check_self_account == "S":
            self.account.savings_balance -= amount
        elif check_self_account != "C" or "S":
            print("Incorrect command. Please try again.")
        if check_other_account == "C":
            other_user.account.balance += amount
        elif check_other_account == "S":
            other_user.account.savings_balance += amount
        elif check_other_account != "C" or "S":
            print("Incorrect command. Please try again.")
        return self



rose = User("Rose", "rose@flowers.com")
tulip = User("Tulip", "tulip@flowers.com")
hydrangea = User("Hydrangea", "hydrangea@flowers.com")



rose.make_deposit(200).open_savings_account().make_deposit(400).make_withdrawal(81).make_deposit(100).display_user_balance()
tulip.make_deposit(800).open_savings_account().make_deposit(700).make_deposit(1200).make_withdrawal(852).make_withdrawal(51).display_user_balance()
hydrangea.open_savings_account().make_deposit(200).make_deposit(700).display_user_balance().transfer_money(150, rose).display_user_balance()
rose.display_user_balance()