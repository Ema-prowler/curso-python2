# Manipular cadenas

nombre = "Ema Prowler"
primer_nombre = nombre[0]
apellido = nombre[4:11]    # con el indice de inicio y el indice final.
# apellido = nombre[4:]    # con el indice de inicio y sin indicar el indice final.
# [4:] Este ultimo toma por defecto hasta el final de la cadena
nombre2 = nombre[0:11:2]    # con el indice de inicio, el indice final y el paso
# el paso es opcional y por defecto es 1
# el paso cuenta el numero de saltos que se van haciendo en la cadena de caracteres.
# nombre2 = nombre[::2]    # version simpificada para obtener la cadena de caracteres cada 2 pasos completa


nombre_invertido = nombre[::-1]    # invertir la cadena de caracteres contando desde el final hacia el inicio


website = "http://www.emaprowler.com"
slice = slice(11,-4)

print(primer_nombre)    # devuelve la letra en el indice indicado

primer_nombre = nombre[0:2]
print(primer_nombre)    # devuelve la letra desde el indice indicado hasta el final del segundo indice indicado
# En este caso el primer indice es inclusivo y el segundo indice es exclusivo
# osea que el segundo indice no tomara en cuenta el ultimo caracter

primer_nombre = nombre[0:3]
print(primer_nombre)    # devuelve la letra desde el indice indicado hasta el final del segundo indice indicado

print(apellido)

print(nombre2) # devuelve la cadena de caracteres cada 2 pasos o saltos

print(nombre_invertido) # devuelve la cadena de caracteres invertida

print(website[slice])

# otra manera de hacerlo
# slice = slice(11,-4)
# sitio = website[slice]
# print(sitio)

