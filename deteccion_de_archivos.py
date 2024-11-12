# deteccion de archivos

import os

path = "D:\\Programacion\\curso-python\\resources\\folder"

if os.path.exists(path):
    print("esa ubicacion existe")
    if os.path.isfile(path):
        print("Es un archivo")
    elif os.path.isdir(path):
        print("Es un directorio")
else:
    print("El archivo no existe")
