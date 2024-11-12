# moviendo archivos

import os

origen = "D:\\Programacion\\curso-python\\resources\\folder"
destino = "D:\\Programacion\\TESTS\\folders"

try:
    if os.path.exists(destino):
        print("ya existe un archivo en este destino")
    else:
        os.replace(origen, destino)
        print(origen + " fue movido a " + destino)
except FileNotFoundError:
    print(origen + " no fue encontrado")



