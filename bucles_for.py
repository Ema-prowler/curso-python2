# Bucles for

#for x in range(50,101,2):
#    print(x)

nombre = input("Ingrese su nombre: ")

for x in nombre:
    print(x)                    # Aquí, `x` se usa para imprimir cada carácter en cada iteración.

# la x solo es una variable temporal.
# el nombre de la variable x se puede modifcar.

# lista de los objetos iterables:

#Cadena (str)	                    "Hola"
#Lista (list)	                    [1, 2, 3]
#Tupla (tuple)	                    (1, 2, 3)
#Conjunto (set)	                    {1, 2, 3}
#Diccionario (dict)	                {"a": 1, "b": 2}
#Rango (range)	                    range(5)
#Archivo (file)	                    open("archivo.txt")
#Generador (generator)	            def generador(): yield ...
#Clases Personalizadas	            class MiIterable: __iter__()