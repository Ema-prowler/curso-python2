# Tipos de datos

# Tipo de dato string.
nombre = "ema"
print(type(nombre)) # la funcion type devuelve el tipo de dato.
print(f"El tipo de dato de la variable que contiene a '{nombre}' es {type(nombre)}") # imprime el tipo de dato
apellido = "fitgerald"
nombreCompleto = "Hola " + nombre + " " + apellido
print(nombreCompleto)  # imprime el nombre completo

# Tipo de dato integer (entero/int) .

edad = 26
print(type(edad))  # imprime el tipo de dato
print(edad)  # imprime el valor de edad

# edad = edad + 1  # metodo comun para sumar un entero
# edad += 1  # metodo simplificado para sumar un entero
# print(edad)  # imprime el valor de edad

print("Tu edad es: " + str(edad))

# Tipo de dato float (decimal/float).

altura = 180.5
print(type(altura))  # imprime el tipo de dato
print(altura)  # imprime el valor de altura
print("Tu altura es: " + str(altura))

# Tipo de dato boolean (verdadero/falso).

humano = True
print(type(humano))  # imprime el tipo de dato
print(humano)  # imprime el valor de humano
humano = False
print(humano)  # imprime el valor de humano
print("Eres un humano: " + str(humano))


