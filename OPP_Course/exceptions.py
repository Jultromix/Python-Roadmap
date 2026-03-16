class LibraryError(Exception):
    pass


class InvalidTitle(LibraryError):
    pass


class BookNotAvailable(LibraryError):
    pass


class UserNotFoundError(LibraryError):
    pass


class InvalidBorrowingQuantity(LibraryError):
    pass
