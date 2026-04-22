import sys
expense_record = "expense.txt"

def show_menu():
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Total Expene")
    print("4.Search Expense")
    print("5.delete Expense")
    print("6.Exit")

def add_expense():
    date = input("Enter Date: ")
    category = input("Enter Category: ")
    amount = int(input("Enter Amount: "))
    description = input("Enter Description: ")
    with open(expense_record,"a") as file:
        file.write(
            f"DATE:{date} CATEGORY:{category} AMOUNT:{amount} DESCRIPTION:{description}\n"
        )
        print("Expense Added Successful")

def view_expense():
    try:
        with open(expense_record,"r") as file:
            data = file.read()
            if not data:
                print("Not Expense Found")
                return
            else:
                print(f"\nExpense Record")
                print(data) 
    except FileNotFoundError:               
        print("File Not Found")

def total_expense():
    total = 0
    try:
        with open(expense_record,"r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                if "AMOUNT:" in line:
                    part1 = line.split("AMOUNT:")
                    part2 = part1[1]
                    amount_part = part2.split("DESCRIPTION:")[0]
                    amount_str = amount_part.strip()
                    amount = int(amount_str)
                total += amount
        print("Total Expense:",total)
    except FileNotFoundError:
        print("File Not Found")         

def search_expense():
    try:
        category = input("Enter Category To Search: ")
        with open(expense_record,"r") as file:
            found = False
            for line in file:
                part = line.split() 
                if category in line:
                    print("\nExpense Found",line)
                    fount = True
            if found == False:
                print("No Record Found")
    except FileNotFoundError:
        print("File Not Found")          

def delete_expense():
    delete_value = input("Enter Category To Delete: ").lower().strip()
    temp_list = []
    found = False
    try:
     with open(expense_record,"r") as file:
        lines = file.readlines()
     for line in lines:
        print("LINE:",line)
        if "CATEGORY:" in line:
            part = line.split("CATEGORY:")[1]
            file_category = part.split()[0].strip().lower()
            print("File Category =>",file_category)
            print("user category =>",delete_value)
            if file_category == delete_value:
                print("match found")
                found = True
                continue
        temp_list.append(line)    

     with open(expense_record,"w") as file:
        file.writelines(temp_list)
     if found:
        print("Expense Deleted Successful")
     else:
        print("Category Not Found")       
    except FileNotFoundError:
        print("File Not Found")                 

def exit():
    sys.exit()


while True:
    show_menu()
    choice = input("Enter Your Choice B/W 1-6: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense() 
    elif choice == "3":
        total_expense() 
    elif choice == "4":
        search_expense()
    elif choice == "5":
        delete_expense() 
    elif choice == "6":
        exit() 
    else:
        print("Invalid Choice Please Try Again")                        
