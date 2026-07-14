def addition(a, b):
    """
    >>> addition(1,2)
    3

    >>> addition(1,-2)
    -1
    """
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    """
    >>> division(10/0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
