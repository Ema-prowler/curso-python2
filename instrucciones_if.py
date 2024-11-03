#Instrucciones if

edad = int(input("Cuantos años tienes? "))

if edad == 100:
    print("Tienes un siglo de vida")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Se puede utilizar else if para realizar multiples condiciones antes de llegar al else final.

# El orden de las instrucciones if, elif y else es importante.
# El programa evaluara las condiciones en el orden en que se escriben.
# Ejecutara la primera condicion que sea verdadera.
# Si no se cumple ninguna condicion, se ejecutara la condicion final(else). si este existe.
