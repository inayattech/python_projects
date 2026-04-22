import sys
contact_record = "contacts.txt"

def show_menu():
    print("1.Add Contact")
    print("2.View Contacts")
    print("3.Search Contact")
    print("4.Delete Contacts")
    print("5.Exit")
def add_contact():
    name = input("Enter Your Name: ")
    phone = int(input("Enter Your Phone No: "))

    with open(contact_record,"a") as file:
        file.write(
            f"Name:{name} | PHONE NUMBER:{phone}\n"
        )
        print("Contact Added")

def view_contact():
    with open(contact_record,"r") as file:
        for line in file:
            print(line.strip()) 

def search_contact():
    name = input("Enter Name To Search: ")
    found = False
    with open(contact_record,"r") as file:
        for line in file:
            clean = line.strip()
            file_name = clean.split(":")[1].strip().lower()
            
            if file_name == name:
                print(clean)
                found = True
                break       
    
    if not found:
        print("Not Found")

def delete_contact():
    del_name = input("Enter Name To Delete: ")
    temp_list = []
    found = False
    with open(contact_record,"r") as file:
        for line in file:
            clean = line.strip()
            file_name = clean.split("|")[0].split(":")[1].strip().lower()
            if file_name != del_name:
                temp_list.append(clean)
            else:
                found = True
    with open(contact_record,"w") as file:
        for line in temp_list:
            file.write(line + "\n")               
        if found:
            print("contact deleted successfully")
        else:
            print("contact Not found")    


def exit():
    print("Programe stopped...")
    sys.exit()


            

while True:
    show_menu()
    choice = input("Enter Your Choice B/W 1-5: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact() 
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        exit()
    else:
        print("Invalid Choice! Please Try Again")                   
        