from library import Library
from users import Student, Professor
from books import PhysicalBook


# Create books
my_book1 = PhysicalBook(
    "The little drunk sailor", "Mariens Sarcowysk", "22223123", True
)
my_book2 = PhysicalBook("Smile face", "Mariens Sarcowysk", "2232845123", True)
my_book3 = PhysicalBook("Red as Murder", "Sarls Moinhanau", "2222341423", True)
my_book4 = PhysicalBook("Laws of Power", "Glea Ahiumy", "356234343", False)
my_book5 = PhysicalBook("Marine Biology", "Suatshme Braf", "443262343", True)
my_book6 = PhysicalBook("Expansionism of space", "Shingeri Fing", "3442367774", False)
my_book7 = PhysicalBook("A<tomic Worlds", "Mosan Sanchez", "1222512345", True)
my_book8 = PhysicalBook("The art of persuasion", "Shasova Petrist", "356672343", True)
my_book9 = PhysicalBook("Kraken, an unseen creature", "Berguir Amil", "22223123", False)
my_book10 = PhysicalBook(
    "The strange case of Martin O' Wayat", "Marton Lumstram", "3342353254", True
)


# Create Students
student1 = Student("Mike", "3324", "Art")
student2 = Student("Anna", "2421", "Math")
student3 = Student("Fin", "1757", "Agronomy")
student4 = Student("Juan", "7382", "Law")
student5 = Student("Jaime", "3835", "Applied Sciences")
student6 = Student("David", "3372", "Medicine")
student7 = Student("Pablo", "0085", "Philosophy")
student8 = Student("Ethan", "2143", "Electronics")
student9 = Student("Gala", "4324", "Software Engineering")
student10 = Student("Marian", "4234", "Music")

book_data: list[PhysicalBook] = [
    my_book1,
    my_book2,
    my_book3,
    my_book4,
    my_book5,
    my_book6,
    my_book7,
    my_book8,
    my_book9,
    my_book10,
]

student_data: list[Student | Professor] = [
    student1,
    student2,
    student3,
    student4,
    student5,
    student6,
    student7,
    student8,
    student9,
    student10,
]
