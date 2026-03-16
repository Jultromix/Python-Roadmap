from books import BookProtocol
from users import RequesterProtocol
from exceptions import BookNotAvailable, UserNotFoundError


class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books: list[BookProtocol] = []
        self.users: list[RequesterProtocol] = []

    def available_books(self):
        return [book for book in self.books if book.availability]

    def search_user(self, id):
        for user in self.users:
            if user.id == id:
                return user

        raise UserNotFoundError(f"The user whose id is: {id}, wasn't found")

    def search_book(self, title):
        for book in self.books:
            if book.title == title and book.availability:
                return book
        raise BookNotAvailable(f"The book: {title} isn't available or doesn't exist")

    @staticmethod
    def validate_isbn(isbn):
        return len(isbn) >= 10
