from exceptions import BookNotAvailable, LibraryError, UserNotFoundError
from books import Book
from library import Library
from users import Professor
from example_data import book_data, student_data
# Create student objects

professor = Professor("Girafales", "23423", "Chemistry")
book1 = Book("The Art of Lying", "Julio Verne", "11111222312232", False)

# Create library
library = Library("Mosan Library")
library.books = book_data
library.users = [professor] + student_data

print("Welcome to Mosans Library")
print("Available books:")

for index, title in enumerate(library.available_books(), start=1):
    print(f"{index}. {title}")

# Search user
try:
    id = input("Type your id number: ")
    user = library.search_user(id)

    print(f" User: {user.name} | ID: {user.id} | Career: {user.career}")
except UserNotFoundError as e:
    print(f"Fail: {e}, {type(e)}")
    print("The searched user doesn't exist")

# Search Book
try:
    title = input("Type the book title: ")
    book = library.search_book(title)
    print(f"Selected book was: {book}")
except BookNotAvailable as e:
    print(f"Fail: {e}, {type(e)}")
    print("The searched book doesn't exist or not available")

# Request book
result = user.request_book(book.title)
print(f"\n{result}")

try:
    result_borrow = book.borrow()
    print(f"\n{result_borrow}")
except BookNotAvailable as e:
    print(e)

# Test error handlers
try:
    result = library.users[0].request_book(None)
    print(f"\n\n\nError handlers start here: \n{result}")
except LibraryError as e:
    print(f"\n\n\nError handlers start here: \nFail: {e}, {type(e)}")
    print("The book request failed")

# Test the not available exception
try:
    print(book1.borrow())
except LibraryError as e:
    print(f"Fail: {e}, {type(e)}")
