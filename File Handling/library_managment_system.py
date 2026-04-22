class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_issued = False

    def display(self):
        print(f"Name:{self.title} Author:{self.author} Available:{self.is_issued}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print("Book Added...")

    def available_book(self):
        for book in self.books:
            if book.is_issued == False:
                print(f"Name:{book.title} Author:{book.author}")

    def issue_book(self,title):
        for book in self.books:
            if book.title == title:
                if book.is_issued == False:
                    book.is_issued = True
                    print("Book Issued")
                    return
                else:
                    print("Already Issued")
                    return               
        print("Book Not Found")     

    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                if book.is_issued == True:
                    book.is_issued = False
                    print("Book Returned")
                    return
                else:
                    print("Book Was Not Issued")
                    return
        print("Book Not Found")  

bok1 = Book("Python","inayat ullah")
bok2 = Book("java","elon musk")
bok3 = Book("sql","harry")

lib = Library()

lib.add_book(bok1)
lib.add_book(bok2)
lib.add_book(bok3)

lib.available_book()

lib.issue_book("Python")

lib.available_book()

lib.return_book("Python")

lib.available_book()


                     