# eliminar archivos

import os
import shutil
path = "D:\\Programacion\\curso-python\\resources\\folder"

try:
    #os.remove(path) # elimina un archivo
    #os.rmdir(path) # elimina el directorio si no contiene archivos dentro
    shutil.rmtree(path) # elimina el directorio y todos sus archivos
except FileNotFoundError:
    print("archivo no encontrado")
except PermissionError:
    print("permiso denegado")
except OSError:
    print("No puedes elminar eso usando esa funcion")
else:
    print(path + " fue eliminado")


