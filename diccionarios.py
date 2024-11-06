# Diccionarios

# un diccionario es una coleccion modificable y no ordenadas de pares unico clave-valor.
# son rapidos porque utilizan el concepto de hash.



capitales = {
             "EE.UU": "Washington D.C.",
             "Argentina":"Buenos Aires",
             "Chile":"Santiago de chile",
             "Brasil":"Brasilia",
             "Cursos":["python", "C++"],
             "anios":22
}


#capitales.update({"Alemania":"Berlin"}) # actualiza un diccionario
#capitales.pop("EE.UU") # borra un elemento del diccionario
#capitales.clear() # borra todos los elementos del diccionario

print(capitales.get("Argenitna")) # devuelve el valor de la clave "EE.UU"
print(capitales.keys()) # devuelve la lista de claves de capitales en este caso.
print(capitales.values()) # devuelve la lista de valores de capitales en este caso.
print(capitales.items()) # devuelve la lista de pares clave-valor de capitales en este caso.

for key,value in capitales.items(): # itera sobre los pares clave-valor de capitales
    print(key,value) # imprime clave y valor de cada par

