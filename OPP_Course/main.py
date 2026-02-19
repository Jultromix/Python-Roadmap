class Book:
    def __init__(self, title: str, author: str, isbn: str, availability: bool):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability
        self.__borrowing_hystory = 0

    def __str__(self):
        return f"title: {self.title} | author: {self.author} | isbn: {self.isbn} | availability: {self.availability}"

    def borrow(self):
        if self.availability:
            self.availability = False
            self.__borrowing_hystory += 1
            return f"{self.title} was borrowed succesfully, borrowing total quantity {self.__borrowing_hystory}"
        return f"{self.title} not available"

    def give_back(self):
        self.availability = True
        return f"{self.title} was returned and is available again"

    def is_popular(self):
        return self.__borrowing_hystory >= 5

    def get_borrowed_quantity(self):
        return self.__borrowing_hystory

    def set_borrowed_quantity(self, borrowed_quantity: int):
        self.__borrowing_hystory = borrowed_quantity


catalog = [
    Book("The Book of Classes", "JM", "123456789", True),
    Book("Cheesecake Recipes", "KV", "234567890", False),
    Book("The Book of Books of Classes", "Dante Visabais", "345678901", True),
    Book("Chemisrty II", "J.v Dallas", "345678901", False),
]

for index, book in enumerate(catalog, start=1):
    print(f"{index} - {book}")

catalog[0].set_borrowed_quantity(23)
print(catalog[0].get_borrowed_quantity())

# print(catalog[0].__borrowing_hystory)     >>> Shows error

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
