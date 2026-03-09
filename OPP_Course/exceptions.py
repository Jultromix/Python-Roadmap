class LibraryError(Exception):
    pass

class InvalidTitle(LibraryError):
    pass

class BookNotAvailable(LibraryError):
    pass