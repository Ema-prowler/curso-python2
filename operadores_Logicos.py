# Operadores lógicos

temperatura = int(input("Cual es la temperatura afuera? : "))

if temperatura >= 0 and temperatura <= 30: # se tienen que cumplir ambas condiciones.
    print("La temperatura esta bien hoy")
elif temperatura < 0 or temperatura > 30: # El operador or verifica si se cumple al menos una de las dos condiciones.
    print("La temperatura esta mal hoy")

# El operador and verifica si se cumplen ambas condiciones.
# El operador or verifica si se cumple al menos una de las dos condiciones.
# El operador not invierte el valor de una epxresion booleana.

# Con booleanos
a = True
b = False

print(not a)  # Imprime False, porque 'a' es True y 'not True' es False.
print(not b)  # Imprime True, porque 'b' es False y 'not False' es True.

# Con comparaciones

x = 10
print(not (x > 5))  # Imprime False, porque 'x > 5' es True y 'not True' es False.
print(not (x < 5))  # Imprime True, porque 'x < 5' es False y 'not False' es True.

# Con condiciones en estructuras de control.
is_raining = False

if not is_raining:
    print("No está lloviendo, podemos salir.")  # Esto se imprimirá porque 'not False' es True.