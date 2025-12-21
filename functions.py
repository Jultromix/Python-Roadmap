from configparser import DuplicateOptionError
from multiprocessing.reduction import duplicate
from tokenize import triple_quoted


def saludar_varaint1(nombre, apellido):   # Argumentos
    print(f"Hola {nombre} {apellido}!")

def saludar_varaint2(nombre="extraño",apellido="desconocido"):
    print(f"Hola {nombre} {apellido}!")
    
saludar_varaint1("Julio","Moreno")   # Saluda a Julio
# saludar_varaint1()          #Saludo generico da error (requiere un argumento forzoso)

saludar_varaint2("Julio","Moreno")   # Saluda a Julio    Parametros
saludar_varaint2()          #Saludo a un extraño

def sumar(a,b):
    return a + b

resultado = sumar(1,1)
print(resultado)


print("------------------------")
#LAMBDA

x = lambda a,b : a+b    
print(x(5,2))

def mifuncion(n):
    return lambda a : a*n

duplicador = mifuncion(2)
triplicador = mifuncion(3)

print(duplicador(5),triplicador(5))
