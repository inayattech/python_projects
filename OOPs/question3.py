class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount}: Deposit Successfull")
            print(f"New Balance:{self.__balance}")
        else:
            print("Amount Must be > 0")    
    def widthraw(self,amount):
        if amount <= self.__balance:     
            self.__balance -= amount
            print(f"{amount}:Widthraw Succssfull")
            print(f"New Balance:{self.__balance}")
        else:
            print("insufficient Balance")    
        
    def get_balance(self):
        return self.__balance

acc = BankAccount("Inayat ullah",5000)    
# print(acc.name)
# #print(acc.balance)
# print(acc.get_balance())

acc.deposit(5000)
acc.widthraw(500)
print(acc.get_balance())




