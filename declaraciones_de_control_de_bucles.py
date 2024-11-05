# Declaraciones de control de bucles break continue pass

# La sentencia break termina completamente el bucle

#nombre = ""

#while True:
#    nombre = input("Ingrese su nombre: ")
#    if nombre != "":
#        break  # termina el bucle

telefono = "123-456-789"

#for i in telefono:
#    if i == "-":
#        continue  # salta el bucle si encuentra el caracter "-" osea sigue a la siguiente iteracion
#    print(i, end="")

for i in range(1,21):
    if i == 13:   #
        pass    # pass actua como un marcador de posicion. No hace nada.
    else:
        print(i)

