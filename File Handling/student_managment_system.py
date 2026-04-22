import sys
file_name = "student.txt"

def shoe_menu():
    print("Student Menu\n")
    print("1. add student")
    print("2. view all student")
    print("3. search student by id")
    print("4. delete student")
    print("Exit")

def add_student():
    user_id = int(input("enter your id: "))
    name = input("enter your name: ")
    
    marks = []
    for mark in range(1,4):
        mark = int(input(f"Enter Your Subject Mark {mark}: "))
        if mark < 0 or mark > 100:
            print("mark must be between 0 to 100")
            return
        marks.append(mark)
    total = sum(marks)
    total_mark = len(marks) * 100
    percentage = (total / total_mark) * 100

    with open(file_name,"a") as file:
        file.write(
            f"ID:{user_id} | NAME: {name} | MARKS: {marks} | TOTAL: {total} | PERCENTAGE: {percentage:.2f}\n"
        )        
        
    print("Add Student Successfull")    

def view_student():
    try:
        with open(file_name,"r") as file:
            data = file.read() 
            if not data:
                print("no data found")
            else:
                print("\n Student Record")
                print(data)
    except FileExistsError:
        print("Not File Found")

def search_student():
    user_id = int(input("Enter ID to search student: ")) 

    fond = False

    try:
        with open(file_name, "r") as file:
            for line in file:
                if f"ID: {user_id} in line":
                    print("Student Found") 
                    print(line)
                    found = True 
                    break
        if not found:
            print("no data found")
    except FileExistsError:
        print("not file found")

def delete_student():
    delete_id = int(input("Enter ID to delete student: "))

    found = False
    try:
        with open(file_name, "r") as file:
            lines = file.readline()

        with open(file_name, "w") as file:
            for line in lines:
                if f"ID: {delete_id}" not in line:
                    file.read(line)
                else:
                    found = True
        if found:
            print("Student Dele" \
            "ted Successful")
        else:
            print("Not Found")
    except FileNotFoundError:
        print("No File Found")
def exit():
    print("program exited")
    sys.exit()


while True:
    shoe_menu()
    choice = input("Enter Your Choice B/W 1-5: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        exit()

    else:
        print("invalid choice please try again")     