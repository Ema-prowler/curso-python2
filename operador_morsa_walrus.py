# Operador morsa walrus "expresion de asignacion"

#print(feliz := True) # asignacion de valor
#print(feliz)

#comidas = []

#while True:
#    comida = input("Que comida te gusta? ")
#    if comida == "salir":
#        break
#    comidas.append(comida)

comidas = []
while (comida := input("Que comida te gusta?")) != 'salir': # esto es una condicion
    comidas.append(comida)

print(comidas)