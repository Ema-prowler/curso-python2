# kwargs

# kwargs es un parametro que empaquetara todos los argumentos en un diccionario
                    # pero asegurate de tener siempre el (**) al principio de tu variable args
# es muy util para que una funcion pueda aceptar una cantidad variable de argumentos de palabras clave

def hola(**kwargs):
    #print("Hola " + kwargs['nombre'] + " " + kwargs['apellido'] + " " + kwargs['segundo_nombre'])
    print("Hola", end=" ")
    for clave, valor in kwargs.items():
        print(valor, end=" ")

hola(titulos = 'senior', nombre="ema", apellido="Prowler", segundo_nombre ="Python")

# Resumen de **kwargs
# **kwargs permite recibir argumentos nombrados variables en forma de diccionario.
# Puedes acceder a estos argumentos en la función como pares clave-valor.
# kwargs.items() permite recorrer todos los pares clave-valor en kwargs.
# Esto hace que el código sea flexible y pueda aceptar cualquier número de argumentos nombrados
# sin necesidad de especificarlos en la definición de la función.