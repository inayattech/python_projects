import hashlib
import getpass
class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def check_password(self,password):
        return self.password == password

class Authsystem:
    def __init__(self):
        self.file_name = "users.txt" 
        self.attempts = {}

   
    def load_user(self):
        user_list = []
        try:
            with open(self.file_name,"r") as file:
                for line in file:
                    line = line.strip()
                    if line == "":
                        continue
                    item = line.split(",")
                    if len(item) < 2:
                        continue
                    username = item[0]
                    password = item[1]
                    user = User(username,password)
                    user_list.append(user)
        except FileNotFoundError:
            print("File Not Found")
        return user_list
    

    def save_user(self,username,password):
        with open(self.file_name,"a") as file:
            file.write(f"{username},{password}\n")
        print("User Saved") 

    def hash_password(self,password):
        hash_value = hashlib.sha256(password.encode()).hexdigest()
        return hash_value       


    def register(self,username,password):
        users = self.load_user()
        for user in users:
            if user.username == username:
                print("User Already Exit")
                return
        hash_pass = self.hash_password(password)    
        self.save_user(username,hash_pass)      
        print("Registered Succssfull")

    def login(self,username,password):
        users = self.load_user()
        found_user = None
        if username not in self.attempts:
            self.attempts[username] = 0

        for user in users:
            if user.username == username:
                found_user = user
                break
        if found_user:        
            while True:
                if self.attempts[username] >= 3:
                    print("Account Locked")
                    return
                hash_pass = self.hash_password(password)
                if found_user.check_password(hash_pass):
                    print("Login Successful")
                    self.attempts[username] = 0
                    return
                else:
                    self.attempts[username] += 1 
                    password = getpass.getpass("Enter Your Password: ")
                       

        else:
            print("user not found")          
                    



auth = Authsystem()
auth.register("inayat","1234")
#auth.register("ali",1122)

auth.login("inayat","124")
