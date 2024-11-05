# test para dibujar un rectangulo

import time

fila = int(input("Ingrese las filas: "))
columnas = int(input("Ingrese las columnas: "))
simbolo = input("ingrese el simbolo: ")

for i in range(fila): # bucle externo
    for j in range(columnas): # bucle interno
        print(simbolo, end=" ")
        time.sleep(1) # Espera 1 segundo entre cada simbolo
    print() # Imprime un salto de linea al final de cada fila

