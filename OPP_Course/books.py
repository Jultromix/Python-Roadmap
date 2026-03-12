from typing import Protocol
from exceptions import BookNotAvailable
from abc import ABC, abstractmethod


class BookProtocol(Protocol):
    def give_back(self) -> str:
        """Method to give back one book"""
        ...

    def borrow(self) -> str:
        """Method to borrow one book"""
        ...

    def calculate_duration(self) -> str:
        """Method to calculate duration"""
        ...


class BaseBook(ABC):
    @abstractmethod
    def give_back(self) -> str:
        """Method to give back one book"""
        pass

    @abstractmethod
    def borrow(self) -> str:
        """Method to borrow one book"""
        pass

    @abstractmethod
    def get_borrowed_quantity(self) -> int:
        """Method to get the borrowed quantity of a book"""
        pass

    @abstractmethod
    def set_borrowed_quantity(self, borrowed_quantity: int):
        """Method to set the borrowed quantity of a book"""
        pass

    @abstractmethod
    def is_popular(self) -> bool:
        """Method to know if a book is popular or not"""
        pass


class Book(BaseBook):
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
        else:
            raise BookNotAvailable(f"The book {self.title} is not available")

    def give_back(self):
        self.availability = True
        return f"{self.title} was returned and is available again"

    def is_popular(self):
        return self.__borrowing_hystory >= 5

    def get_borrowed_quantity(self):
        return self.__borrowing_hystory

    def set_borrowed_quantity(self, borrowed_quantity: int):
        self.__borrowing_hystory = borrowed_quantity


class PhysicalBook(Book):
    def calculate_duration(self):
        return "7 days"


class VirtualBook(Book):
    def calculate_duration(self):
        return "14 days"
