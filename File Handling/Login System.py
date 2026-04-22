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
        for user in users:
            if user.username == username:
                found_user = user
        if found_user:        
            counter = 0 
            while counter < 3:
                hash_pass = self.hash_password(password)
                if found_user.check_password(hash_pass):
                    print("login succssful")
                    return
                else:
                    counter += 1
                    if counter < 3:
                        print("total 3 attempt")
                        password = getpass.getpass("Try Again:")
                        print("Remaining Attempt",3-counter)
                    else:
                        print("Limit Reached")
                        return
        else:
            print("user not found")          
                    



auth = Authsystem()
auth.register("inayat","1234")
#auth.register("ali",1122)

auth.login("inayat","1234")
