# Funciones lambda

# Ejemplo 1
#def doble(x):
#    return x * 2

#print(doble(5))
#-----------------

#doble = lambda x: x * 2
#
#print(doble(5))

#-----------------

# Ejemplo 2

multiplicar = lambda x, y: x * y

print(multiplicar(5, 6))

#-----------------

# Ejemplo 3

suma = lambda x, y, z: x + y + z
print(suma(5, 6, 7))

#-----------------

# Ejemplo 4

nombre_completo = lambda nombre, apellido: nombre + " " + apellido

print(nombre_completo("Ema", "Prowler"))

#-----------------

# Ejemplo 5

check_edad = lambda edad: True if edad >= 18 else False
print(check_edad(15))