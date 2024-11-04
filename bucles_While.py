# Bucles while

nombre = ""

#while len(nombre) == 0: #
#    nombre = input("Ingrese su nombre: ")

#while not nombre:
#    nombre = input("Ingrese su nombre: ")

while not nombre or len(nombre) == 0:
    nombre = input("Ingrese su nombre: ")

print("Hola " + nombre)

# Inicialmente la variable nombre esta vacia.
# Se le pide al usuario que ingrese su nombre.
# Si el nombre es vacio, se le pide de nuevo.
# Si el nombre no es vacio, se sale del bucle.

# Se puede utilizar el operador not para verificar si una variable es falsa.
# El operador not invierte el valor de una epxresion booleana.
# por lo que si nombre es vacio el bucle continuara.
