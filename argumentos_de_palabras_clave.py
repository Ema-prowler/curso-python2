# Argumentos de palabras clave

# En los argumentos de palabras clave no importa el orden.
# En los posicionales si importa el orden.


def saludo(nombre, apellido, lenguaje):
    print("Hola " + nombre + " " + apellido + ", estas aprendiendo: " + lenguaje)

#saludo("ema" , "prowler", "Python") # El orden es importante (Posicionales)
saludo(lenguaje = "Python" , nombre = "ema" , apellido = "prowler") # El orden no es importante en las (Palabras clave)