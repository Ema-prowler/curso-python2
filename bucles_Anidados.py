# Bucles anidados

# un bucle interno finalizara antes de que finalize el bucle externo.

fila = int(input("Cuantas filas quieres? "))
columnas = int(input("Cuantas columnas? "))
simbolo = input("Ingrese el simbolo: ")

for i in range(fila):   #bucle externo
    for j in range(columnas):   #bucle interno
        print(simbolo, end="")
    print()