# Sets

# Los sets son una estructura de datos usada para almacenar elementos similares a las listas.

# 1 los elementos de un set son unicos y no pueden haber duplicados
# 2 los sets son desoradenados, no mantienen el orden de cuando son declarados.
# 3 Sus elementos deben ser inmutables.

# Un conjunto de sets es mas rapido que un conjunto de listas.



utensilios = {"tenedor","cuchara","cuchillo"}
platos = {"plato","bol","taza","cuchara"}


# utensilios.add("cucharita")  # Para agregar un elemento a un set
# utensilios.remove("tenedor") # para borrar un elemento de un set
# utensilios.pop() # borra un elemento random del set
# utensilios.clear() # borra todos los elementos del set

# utensilios.update(platos)  # actualiza un set con otro set agregando los elementos del set platos
#print(utensilios.difference(platos)) # nos devuelve la diferencia
print(utensilios.intersection(platos)) # nos devuelve la interseccion

#for x in utensilios:
#    print(x)  # se imprime en orden desordenado.

