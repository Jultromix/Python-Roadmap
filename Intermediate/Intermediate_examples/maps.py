numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num**2)

print(numbers)
print(squares)


def square(num):
    return num**2


squares_map = list(map(square, numbers))

print(squares_map)
