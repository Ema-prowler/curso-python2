# leer un archivo

try:
    with open("D:\\Programacion\\curso-python\\resources\\test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("Archivo no encontrado")

#print(file.closed)  # True si el archivo ha sido cerrado
