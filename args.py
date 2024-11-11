# args

# args es un parametro que empaquetara todos los argumentos en una tupla
                    # pero asegurate de tener siempre el (*) al principio de tu variable args
def suma(*args):   #args es una abreviatura de argumentos puedes cambiar la palabra si quieres.
    suma = 0
    cosas = list(args)
    cosas[0] = 0
    for i in cosas:
        suma += i
    return suma


print(suma(1, 5,3,2,7,1))

#Este código:

#Toma una cantidad indefinida de argumentos.
#Ignora el primer valor, reemplazándolo con 0.
#Suma los valores restantes y devuelve el total.