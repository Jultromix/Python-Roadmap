from exceptions import LibraryError, UserNotFoundError
from books import PhysicalBook, Book
from library import Library
from users import Student, Professor
from example_data import book_data, student_data
# Create student objects

professor = Professor("Girafales", "23423", "Chemistry")
book1 = Book("The Art of Lying", "Julio Verne", "11111222312232", False)

# Create library
library = Library("Mosan Library")
library.books = book_data
library.users = [professor] + student_data

for user in library.users:
    print(user.request_book("The Art of Lying"))

print("Welcome to Mosans Library")
print("Available books:")

for index, title in enumerate(library.available_books(), start=1):
    print(f"{index}. {title}")


try:
    id = input("Type your id number: ")
    user = library.search_user(id)

    print(f" User: {user.name} | ID: {user.id} | Career: {user.career}")
except UserNotFoundError as e:
    print(f"Fail: {e}, {type(e)}")
    print("The searched user doesn't exist")


# Test error handlers
try:
    result = student.request_book(None)
    print(f"\n\n\n Error handlers start here: \n{result}")
except LibraryError as e:
    print(f"\n\n\nError handlers start here: \nFail: {e}, {type(e)}")
    print("The book request failed")

# Test the not available exception
try:
    print(book1.borrow())
except LibraryError as e:
    print(f"Fail: {e}, {type(e)}")
