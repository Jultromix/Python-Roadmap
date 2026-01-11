a = 0
b = 0
result = None

try:
    a = int(input("Add a number "))
    b = int(input("Add a number "))
except Exception as e:
    print("What you typed is not a number")
    print(f"error: {e} | error type: {type(e)}")

try:
    result = a / b
except Exception as e:
    print("Division by 0 not allowed")
    print(f"error: {e} | error type: {type(e)}")

print(f"Result: {result}")

### A cleaner and specific version of capturing exceptions should be
a = 0
b = 0
result = None

try:
    a = int(input("Add a number "))
    b = int(input("Add a number "))
    result = a / b
    print(f"Result: {result}")
except ValueError:
    print("What you typed is not a number")
except ZeroDivisionError:
    print("It's not allowed to divide by 0")
