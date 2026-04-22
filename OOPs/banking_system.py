class Bankaccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def show_balance(self):
        return f"{self.name} Ka Balance Ha {self.balance}"
    
    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} Deposit")
        print(f"New Balance:{self.balance}")

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount}:Withdraw Successful")
            print(f"New Balance:{self.balance}")
        else:
            print("Insufficient Balance")    

class SpecialAccount(Bankaccount):
    def add_interest(self,rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print(f"{rate} interested added {interest}")
        print(f"New Balance:{self.balance}")



account1 = SpecialAccount("inayat ullah",1000)
account1.deposit(500)
account1.withdraw(500)
account1.add_interest(10)
account1.show_balance()

# result = Bankaccount("inayat Ullah",500)  

# print(result.show_balance())

# result.deposit(500)
# result.withdraw(100)

# print(result.show_balance())
        