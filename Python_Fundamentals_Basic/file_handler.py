# Reading file content
try:
    with open("archivo.txt","r",encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    open("archivo.txt","x")
    print("No se pudo abrir el archivo")

# Modifying file content
try:
    with open("archivo.txt","w") as f:
        f.write("File has been modified")
    with open("archivo.txt","r",encoding="utf-8") as f:
        print(f.readline())
except FileNotFoundError:
    open("archivo.txt","x")
    print("No se pudo abrir el archivo")

# Adding more content
try:
    with open("archivo.txt","a") as f:
        f.write("File has been modified")
    with open("archivo.txt","r",encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    open("archivo.txt","x")
    print("No se pudo abrir el archivo")