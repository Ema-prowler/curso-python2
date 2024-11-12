# modulo random

import random

x = random.randint(1, 6)  # genera un numero aleatorio entre 1 y 6
y = random.random()  # genera un numero aleatorio entre 0 y 1

mi_lista = ["piedra", "papel", "tijera",] # LISTA de elementos
z = random.choice(mi_lista)  # elegir un elemento aleatorio de la lista

cartas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"] # LISTA de cartas

random.shuffle(cartas)  # mezcla los elementos de la lista


print(x)
print(y)
print(z)
print(cartas)