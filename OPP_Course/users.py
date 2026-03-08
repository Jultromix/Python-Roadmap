from typing import Protocol
from main import Book

class RequesterProtocol(Protocol):
    def request_book(self, title: str) -> str:
        """Method to be used by any requester"""
        ...

class User():
    def __init__(self,name:str, id:int):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def request_book(self, title:str):
        return f"Book {title} request done"
    
    def return_book(self, title):
        if len(self.borrowed_books) > 0 and title in self.borrowed_books:
            self.borrowed_books.remove(title)
            return f"Book: {title} was returned successfully, borrowed books: {len(self.borrowed_books)}"
        else:
            return f"There are no more books to return"

class Student(User):
    def __init__(self, name, id, career):
        super().__init__(name, id)
        self.career = career
        self.book_limit = 3
        self.borrowed_books = []

    def request_book(self, title):
        if len(self.borrowed_books) < self.book_limit:
            self.borrowed_books.append(title)
            return f"Book: {title} was borrowed successfully, borrowed books: {len(self.borrowed_books)}"
        else:
            return f"No more books can be borrowed, limit has been reached: {self.book_limit}"
        


class Professor(User):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department
        self.book_limit = None

    
    def request_book(self, title):
        self.borrowed_books.append(title)
        return f"Book: {title} was borrowed successfully, borrowed books: {len(self.borrowed_books)}"
        
        

student = Student("Mike", 1223, "Art")
student_1 = Student("Jose", 1224, "Math")
professor = Professor("Girafales", 23423, "Chemistry")
book = Book("The Art of Lying", "Julio Verne", "11111222312232")

users: list[RequesterProtocol] = [student, student_1,professor, book]

for user in users:
    print(user.request_book("The Art of Lying"))