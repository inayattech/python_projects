class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
        self.__marks = []

    def add_mark(self,mark):
        if mark < 0 or mark > 100:
            print("Invalid Mark")
            return
        if len(self.__marks) > 3:
            print("Cannot Add More Then 3 Subjects")
            return
        self.__marks.append(mark)

    def average(self):
        if not self.__marks:
            return 0
        return sum(self.__marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if not self.__marks:
            return "No Grade"
        elif avg >= 80:
            return "A"
        elif avg >= 60 and avg < 80:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"
        
    def get_marks(self):
        return self.__marks

std = Student("inayat",32)
std.add_mark(90)
std.add_mark(80)
std.add_mark(100)    

print(std.average())
print(std.grade())


