from exceptions import LibraryError
from books import PhysicalBook, Book
from library import Library
from users import Student, Professor

# Composition Examples:
my_book = PhysicalBook("The little drunk sailor", "Mariens Sarcowysk", "22223123", True)
my_book_unavailable = PhysicalBook(
    "The big fancy river", "Stephen Wallow", "3342123", False
)
another_book = PhysicalBook(
    "K'otongasin Lan Venderdier", "Marshell Billow", "4411231", True
)

# Create library
library = Library("Mosan Library")
library.books = [my_book, my_book_unavailable, another_book]
print(library.available_books())

catalog = [
    Book("The Book of Classes", "JM", "123456789", True),
    Book("Cheesecake Recipes", "KV", "234567890", False),
    Book("The Book of Books of Classes", "Dante Visabais", "345678901", True),
    Book("Chemisrty II", "J.v Dallas", "345678901", False),
]

# Usage of enumarate while showing information of "catalog"
for index, book in enumerate(catalog, start=1):
    print(f"{index} - {book}")

# Usage of set() and get() functions
# catalog[0].set_borrowed_quantity(23)
# print(catalog[0].get_borrowed_quantity())

# print(catalog[0].__borrowing_hystory)     >>> Shows error

# Test the not available exception
try:
    print(catalog[1].borrow())
except LibraryError as e:
    print(f"Fail: {e}, {type(e)}")

# print(catalog[0].borrow())
# print(catalog[0].give_back())
# print(catalog[0].borrow())
# print(catalog[0].give_back())
# print(catalog[0].borrow())
# print(catalog[0].give_back())
# print(catalog[0].borrow())
# print(catalog[0].give_back())
# print(catalog[0].is_popular())
# print(catalog[0].borrow())
# print(catalog[0].give_back())
# print(catalog[0].is_popular())

# Create student objects
student = Student("Mike", 1223, "Art")
student_1 = Student("Jose", 1224, "Math")
professor = Professor("Girafales", 23423, "Chemistry")
book = Book("The Art of Lying", "Julio Verne", "11111222312232", True)

library.users = [student, student_1, professor]
for user in library.users:
    print(user.request_book("The Art of Lying"))

# Test error handlers
try:
    result = student.request_book(None)
    print(result)
except LibraryError as e:
    print(f"Fail: {e}, {type(e)}")
    print("The book request failed")
