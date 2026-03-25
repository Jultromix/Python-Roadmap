set_countries = {"Russia", "USA", "China", "India", "Brazil"}
print(set_countries, type(set_countries))

set_numbers = {1, 2, 3, 4, 5, 2}
print(set_numbers)

set_tyes = {1, "Hello", 3.14, (1, 2)}
print(set_tyes)

set_from_String = set("Hello")
print(set_from_String)

set_from_tuple = set(("abc", "def", "abc", "cbv"))
print(set_from_tuple)

numbers = {1, 2, 3, 4, 5}
set_numbers = set(numbers)
unique_numbers = list(set_numbers)
print(set_numbers, unique_numbers)
