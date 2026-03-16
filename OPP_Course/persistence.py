import json
from books import PhysicalBook
from users import Student, Professor
from datetime import datetime
from library import Library


class Persistence:
    def __init__(self, file="library_data.json") -> None:
        self.file = file

    def save_data(self, library):
        data = {
            "name": library.name,
            "users": [users.__dict__ for users in library.users],
            "books": [books.__dict__ for books in library.books],
            "saved_data": datetime.now().isoformat(),
        }

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_data(self):
        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f)
            # return data

        library = Library(data["name"])

        for book_data in data["books"]:
            book = PhysicalBook(
                title=book_data["title"],
                author=book_data["author"],
                isbn=book_data["isbn"],
                availability=book_data["availability"],
            )
            library.books.append(book)

        for user_data in data["users"]:
            if "career" in user_data:
                user = Student(
                    name=user_data["name"],
                    id=user_data["id"],
                    career=user_data["career"],
                )
            else:
                user = Professor(
                    name=user_data["name"],
                    id=user_data["id"],
                    department=user_data["department"],
                )
            library.users.append(user)
            return library
