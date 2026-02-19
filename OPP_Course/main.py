class Book:
    def __init__(self, title: str, author: str, isbn: str, availability: bool):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability
        self.borrowing_hystory = []

    def __str__(self):
        return f"title: {self.title} | author: {self.author} | isbn: {self.isbn} | availability: {self.availability}"

    def borrow(self):
        if self.availability:
            self.availability = False
            self.borrowing_hystory.append(self)
            return f"{self.title} was borrowed succesfully"

    def give_back(self):
        self.availability = True
        return f"{self.title} was returned and is available again"

    def is_popular(self):
        return self.borrowing_hystory.count(self) >= 5


catalog = [
    Book("The Book of Classes", "JM", "123456789", True),
    Book("Cheesecake Recipes", "KV", "234567890", False),
    Book("The Book of Books of Classes", "Dante Visabais", "345678901", True),
    Book("Chemisrty II", "J.v Dallas", "345678901", False),
]

for index, book in enumerate(catalog, start=1):
    print(f"{index} - {book}")

print(catalog[0].borrow())
print(catalog[0].give_back())
print(catalog[0].borrow())
print(catalog[0].give_back())
print(catalog[0].borrow())
print(catalog[0].give_back())
print(catalog[0].borrow())
print(catalog[0].give_back())
print(catalog[0].is_popular())

print(catalog[0].borrow())
print(catalog[0].give_back())
print(catalog[0].is_popular())
