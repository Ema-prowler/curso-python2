# Funcion de orden superior

#ejemplo 1

def hablarAlto(texto):
    return texto.upper()

def hablarBajo(texto):
    return texto.lower()

def hola(func):   # las funciones en python se consideran como objetos
    texto = func("Hola")
    print(texto)


hola(hablarAlto)
hola(hablarBajo)
