class Book:
    def __init__(self, title: str, author: str, isbn: str, availability: bool):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability


catalog = [
    Book("The Book of Classes", "JM", "123456789", True),
    Book("Cheesecake Recipes", "KV", "234567890", False),
    Book("The Book of Books of Classes", "Dante Visabais", "345678901", True),
    Book("Chemisrty II", "J.v Dallas", "345678901", False),
]

for index, book in enumerate(catalog, start=1):
    print(
        f"{index} - title: {book.title} | author: {book.author} | isbn: {book.isbn} | availability: {book.availability}"
    )
