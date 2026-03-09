from books import BookProtocol
from users import RequesterProtocol


class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books: list[BookProtocol] = []
        self.users: list[RequesterProtocol]  = []

    def available_books(self):
        return [
            book.title
            for book in self.books
            if book.availability
        ]
