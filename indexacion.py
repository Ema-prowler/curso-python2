# Indexacion

nombre = "ema prowler!"

#if nombre [0].islower(): # si el primer caracter es minuscula
#    nombre = nombre.capitalize() # lo cambia a mayusculas

primer_nombre = nombre[0:3].upper()  # Con el operador de indice especificamos un rango para acceder a los elementos.
# del 0 al 3. lo convertimos a mayusculas y lo asignamos a una nueva varable primer_nombre
# Se puede omitir el indicie de inicio para que tome por defecto desde el inicio o desde 0

apellido = nombre[4:].lower()
ultimo_caracter = nombre[-1]


print(primer_nombre)
print(apellido)
print(ultimo_caracter)



#print(nombre)