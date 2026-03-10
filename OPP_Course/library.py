from books import BookProtocol
from users import RequesterProtocol
from exceptions import UserNotFoundError


class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.books: list[BookProtocol] = []
        self.users: list[RequesterProtocol] = []

    def available_books(self):
        return [book.title for book in self.books if book.availability]

    def search_user(self, id):
        for user in self.users:
            if user.id == id:
                return user

        raise UserNotFoundError(f"The user whose id is: {id}, wasn't found")
