"""Typing with Python"""

from doctest import Example


variable = 42  # It's idenified as int
print(f"variable: {variable}, of type: {type(variable)}")

# Traditional syntaxis variable = value
# Type hint syntaxis variable : type = value

other_var: int = 44
print(f"variable: {other_var}, of type: {type(other_var)}")

user_id: int | None = None

user_id = None


def clear_sum(a: int, b: int) -> int:
    return a + b


print(clear_sum(2, 2))

articles_1: list[dict] = [{"title": "example1"}, {"title": "example2"}]
articles_2: list[list[str]] = [["example1"], ["example2"]]

from typing import Any

articles_3: list[list[Any]] = [["example1"], ["example2"]]

articles_1
articles_2
articles_3


def example_function() -> str:
    """This is the description of the function
    Description
    Args
    Returns:
        str: an example string
    Exceptions
    Examples
    """
    return "example"


print(example_function.__doc__)
help(example_function)
