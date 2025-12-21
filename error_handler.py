try:
    num = 10/0
    print("try something")
except ZeroDivisionError:
    print("Divided by cero")

try:
    print(x)
except NameError:
    print("Undefined variable")
finally:
    print("this will executed no matter if an error was present or not")