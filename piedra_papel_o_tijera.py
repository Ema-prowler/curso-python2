# Piedra, papel o tijera

import random

lista = ["piedra", "papel", "tijera"] # lista de opciones



while True:
    computadora = random.choice(lista)  # selecciona una opcion aleatoria
    jugador = None  # variable que almacenara la opcion del jugador empieza en None

    while jugador not in lista:  # mientras el jugador no sea una opcion del lista
        jugador = input("piedra, papel o tijera?: ").lower()  # pide la opcion del jugador y la convierte a minusculas

    if jugador == computadora:  # si el jugador es igual a la computadora
        print("computadora: " + computadora)
        print("jugador: " + jugador)
        print("empate")
    elif jugador == "piedra":
        if computadora == "papel":
            print("computadora: " + computadora)
            print("jugador: " + jugador)
            print("Perdiste")
        if computadora == "tijera":
            print("computadora: " + computadora)
            print("jugador: " + jugador)
            print("Ganaste")
    elif jugador == "papel":
        if computadora == "tijera":
            print("computadora: " + computadora)
            print("jugador: " + jugador)
            print("Perdiste")
        if computadora == "piedra":
            print("computadora: " + computadora)
            print("jugador: " + jugador)
            print("Ganaste")
    elif jugador == "tijera":
        if computadora == "piedra":
            print("computadora: " + computadora)
            print("jugador: " + jugador)
            print("Perdiste")
        if computadora == "papel":
            print("computadora: " + computadora)
            print("jugador: " + jugador)
            print("Ganaste")

    jugar_de_nuevo = input("Quieres jugar de nuevo? (si/no): ").lower()

    if jugar_de_nuevo != "si":
        break

print("adios")