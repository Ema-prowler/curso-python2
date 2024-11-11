# Ambito de las variables

# el ambito de una variable es la region en la que una variable es reconocida.
# una variable esta disponible dentro de la region en la que se crea/declara

nombre = "prowler"


def mostrar_nombre():
    #nombre = "ema"
    print(nombre)
    # si no hay variable local, python utilizara la variable mas cercana
    # utilizando la regla LEGB (Local, Encapsulated, Global, Built-in)
    # o Local, Variables cercanas, variables globales y variables integradas.
    # Orden
    # Local
    # Envolvente
    # Global
    # Incorporado
    #--------------------------


mostrar_nombre()

# es posible tener una variable local y una global con el mismo nombre

#--------------------------
#nombre solo esta disponible dentro de la funcion mostrar_nombre
#print(nombre) # por eso aqui da error al tratar de imprimir el nombre
#--------------------------


