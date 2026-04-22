class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount}:Deposit Succssful") 
            print(f"New Balance:{self.__balance}") 
        else:
            print("Amount Must Be > 0")      

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount}:Withdraw Succssful") 
            print(f"New Balance:{self.__balance}") 
            return True
        else:
            print("insufficient Balance")
            return False    


    def get_balance(self):
        return self.__balance
    
class Bank:
    def __init__(self,bank_name):
        self.bank_name = bank_name
        self.accounts = []

    def add_account(self,account):
        if isinstance(account,BankAccount):
            self.accounts.append(account)   
            print("Account Added Succssful")   
        else:
            print("Invalid Account Objects")
   
    def transfer(self,sender,receiver,amount):
        if amount <= 0:
            print("Invalid Amount")
            return
        if sender not in self.accounts:
            print("Sender Account Not Fount")
            return
        if receiver not in self.accounts:
            print("Reveiver Account Not Found")
            return
        if sender.withdraw(amount):
            receiver.deposit(amount)
            print("File Transfer Succssful")  
        else:
            print("Transfer Field")      


    
acc1 = BankAccount("Inayat Ullah",5000) 
acc2 = BankAccount("ali",10000)

bank = Bank("mybank")
bank.add_account(acc1)
bank.add_account(acc2)

bank.transfer(acc1,acc2,1000)
          