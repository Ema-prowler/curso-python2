# Listas 2D

# Las listas 2D son listas separadas por comas.

bebidas = ["cafe", "soda", "te"]
cena = ["pizza","Hamburguesa","Hot Dog"]
postres = ["pastel","helado"]

comida = [bebidas, cena, postres] # lista de listas

print(comida)
print(comida[0])  # Imprime la lista de bebidas que corresponde al indice 0
print(comida[2][1])  # Imprime el primer elemento de la lista de bebidas


# cuando creamos una lista de listas, lo que contenga la lista comida
# en este caso son las otras listas que a su vez son los elementos de la lista comida.
# en este caso comida tiene 3 elementos, bebidas, cena y postres.

# comida = [
#    ["cafe", "soda", "te"],        # Elemento 0: lista de bebidas
#    ["pizza", "Hamburguesa", "Hot Dog"],  # Elemento 1: lista de cenas
#    ["pastel", "helado"]          # Elemento 2: lista de postres
# ]