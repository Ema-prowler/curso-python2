# Copiando archivos

# copyfile()
# copy()
# copy2()

import shutil

#shutil.copyfile(origen,destino)
shutil.copy("D:\\Programacion\\curso-python\\resources\\test.txt","D:\\Programacion\\curso-python\\resources\\copy.txt")

# Ejemplos:

# Copia solo el contenido del archivo de origen al archivo de destino
# Sobrescribe el archivo de destino si ya existe.
# shutil.copyfile("ruta/origen.txt", "ruta/destino.txt")

# Resumen: copyfile copia únicamente el contenido del archivo de origen al archivo de destino.
# No copia permisos ni metadatos.

# Uso común: Se usa cuando solo necesitas el contenido y el archivo de destino puede ser sobrescrito.

# Copia el contenido y los permisos del archivo de origen al archivo de destino
# Sobrescribe el archivo de destino si ya existe.
# shutil.copy("ruta/origen.txt", "ruta/destino.txt")

# Resumen: copy copia tanto el contenido como los permisos del archivo de origen al destino,
# pero no copia los metadatos detallados, como la fecha de creación.
# Uso común: Ideal cuando necesitas mantener los permisos del archivo original,
# pero no necesitas conservar los metadatos adicionales.


# Copia el contenido, permisos y metadatos (fechas, etc.) del archivo de origen al archivo de destino
# Sobrescribe el archivo de destino si ya existe.
# shutil.copy2("ruta/origen.txt", "ruta/destino.txt")


# Resumen: copy2 copia el contenido, los permisos y todos los metadatos del archivo
# (como fecha de modificación y creación).
# Uso común: Se usa cuando deseas una copia exacta que incluya tanto los permisos
# como los metadatos originales.


# Diferencias Clave
# copyfile(): Copia solo el contenido.
# copy(): Copia contenido y permisos.
# copy2(): Copia contenido, permisos y todos los metadatos adicionales.


# Si solo queremos el contenido
# shutil.copyfile("ruta/origen.txt", "ruta/destino.txt")

# Si queremos contenido y permisos
# shutil.copy("ruta/origen.txt", "ruta/destino.txt")

# Si queremos una copia completa, incluyendo fechas y otros metadatos
# shutil.copy2("ruta/origen.txt", "ruta/destino.txt")