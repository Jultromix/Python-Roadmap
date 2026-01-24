# a = 0
# b = 0
# result = None

# try:
#     a = int(input("Add a number "))
#     b = int(input("Add a number "))
# except Exception as e:
#     print("What you typed is not a number")
#     print(f"error: {e} | error type: {type(e)}")

# try:
#     result = a / b
# except Exception as e:
#     print("Division by 0 not allowed")
#     print(f"error: {e} | error type: {type(e)}")

# print(f"Result: {result}")


class DivisionError(Exception):
    """ "Error in operation"""

    pass


### A cleaner and specific version of capturing exceptions should be
a = 0
b = 0
result = None

try:
    a = int(input("Add a number "))
    b = int(input("Add a number "))
    if b == 2:
        raise DivisionError("Custom_Division_by_2_Error")
    result = a / b
    print(f"Result: {result}")
except ValueError:
    print("What you typed is not a number")
except ZeroDivisionError:
    print("It's not allowed to divide by 0")
finally:
    print("print from finally")

print("print out of error handlers")
