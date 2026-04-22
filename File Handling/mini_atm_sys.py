# Mini Atm System

class BankAccount:
    def __init__(self, name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print("Deposit:",amount)
            print("Balance After Deposit:",self.balance)
        else:
            print("invalid amount")
    def withdraw(self,amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print("Withdraw:",amount)
            print("Balance After Withdraw:",self.balance)
        else:
            print("Insufficient Balance")    
    def get_balance(self):
        print("Balance", self.balance)

class Atm:
    def __init__(self):
        self.accounts = []  

    def add_account(self,account):
        self.accounts.append(account)

    def find_account(self,account):
        for acc in self.accounts:
            if acc.name == account.name:
                return acc


ba1 = BankAccount("inayat",5000)
ba2 = BankAccount("zain",10000)

ba1.deposit(2000)
ba1.withdraw(1000)

ba1.get_balance()

atm_obj = Atm()
atm_obj.add_account(ba1)




