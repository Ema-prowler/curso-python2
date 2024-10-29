# Ingresar texto

nombre = input("Cual es tu nombre: ") # toma el texto ingresado por el usuario
edad = int(input("Cuantos años tienes: ")) # convierte el valor ingresado a un numero tipo entero (int)
altura = float(input("Que tan alto eres: ")) # Convierte el valor ingresado a un numero tipo float (float)

edad = edad + 1

print("Hola " + nombre)  # imprime el texto ingresado por el usuario
print("Tienes " + str(edad) + " años")
print("Mides  " + str(altura) + " CM")