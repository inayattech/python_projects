class Employee:
    def __init__(self,name,salary,department):
        self.name = name
        self.__salary = salary
        self.department = department
    def get_salary(self):
        return self.__salary    
    
    def set_salary(self,new_salary):
        self.new_salary = new_salary
        if new_salary > 0:
            self.__salary = new_salary
            print("Salary Update Successful")
        else:
            print("Value Must Be > zero")

acc = Employee("inayat ullah",2500,"IT")   
acc.set_salary(50000)
print(acc.get_salary())