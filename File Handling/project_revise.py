import sys
file_name = "student_record.txt"

def show_menu():
    print("Student Menu")
    print("1. add student")
    print("2. view all student")
    print("3. search student by id")
    print("4. delete student")
    print("5. exit")

def add_student():
    student_id = int(input("enter your id: "))
    name = input("enter your name: ") 

    marks = [] 
    for mark in range(1,4):
        mark = int(input(f"enter your subject mark {mark}: "))
        if mark < 0 or mark > 100:
            print("marks must be between 0 t(o 100")
        marks.append(mark)
    total = sum(marks)
    percentage = total / 300 * 100

    with open(file_name,"a") as file:
        file.write(
            f"ID: {student_id} | NAME: {name} | MARKS: {marks} | TOTAL: {total} | PERCENTAGE: {percentage:.2f}"
        )
        print("Student Added Successful")

def view_student():
    try:
        with open(file_name,"r") as file:
            data = file.read()
            if not data:
                print("no data found")
            else:
                print("Student Record")
                print(data)
    except FileNotFoundError:
        print("file not found")            

def search_student():
    search_id = int(input("Enter Id to search: "))

    found = False
    try:
        with open(file_name, "r") as file:
            for line in file:
                if f"ID: {search_id}" in line:
                    print(line)
                    found = True
                    break
        if not found:
            print("no data found")
    except FileNotFoundError:
        print("file not found")

def delete_student():
    search_id = int(input("Enter id to search:"))

    found = False

    try:
        with open(file_name,"r") as file:
            lines = file.readline()
        with open(file_name,"w") as file:
            for line in lines:
                if "ID: {search_id}" not in line:
                    file.read(line)
                    found = True
            if found:
                print("student deleted successfull")
    except FileNotFoundError:
        print("file not found")

def exit():
    print("program exited")
    sys.exit() 


while True:
    show_menu()
    choice = input("Enter your choice: ")
    
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
        print("invalid choice try again")                 

                            