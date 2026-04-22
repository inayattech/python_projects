class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = []

    def add_mark(self,mark):
        if len(self.marks) >= 3:
            print("Cannot Add More Than 3 Objects Mark")
            return
        if mark < 0 or mark > 100:
            return "Invalid Marks"
        else:
            self.marks.append(mark)

    def average(self):
        if not self.marks:
            return 0
        total = sum(self.marks)
        lenth = len(self.marks)
        return total / lenth
        

    def grade(self):
        avg = self.average()

        if not self.marks:
            return "No Grade"
        if avg >= 80:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"
    def display(self):
        print(f"Name:{self.name} | Roll No:{self.roll_no} | Marks:{self.marks} | Average:{self.average()} | Grade:{self.grade()}")


class School:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        if isinstance(student,Student):
            self.students.append(student)
            print("Student Added")    
        else:
            print("Invalid Student")    

    def find_student(self,roll_no):
        for std in self.students:
            if std.roll_no == roll_no:
                return std
        return None
    
    def find_topper(self):
        topper = self.students[0]
        for student in self.students:
            if student.average() > topper.average():
                topper = student
        return topper   

    def fail_student(self):
        fail = []
        for student in self.students:
            if student.grade() == "Fail":
                fail.append(student)
        return fail        

    def search_name(self,name):
        for student in self.students:
            if student.name == name:
                return student
        return None    



    def show_all_student(self):
        for std in self.students:
            std.display()            

std1 = Student("Inayat",232)
std2 = Student("zain",25)
std1.add_mark(90)
std1.add_mark(80)
std1.add_mark(70)
std2.add_mark(90)
std2.add_mark(90)
std2.add_mark(90)
std2.add_mark(90)
std1.add_mark(90)
sch = School()

sch.add_student(std1)
sch.add_student(std2)

sch.find_topper()
sch.show_all_student()

# std.average()
# std.grade()
# std.display()


