# Pasar objetos como argumentos

class Coche:
    color = None #variable de clase

class Motocicleta:
    color = None #variable de clase

def cambiar_color(vehiculo, color):
    vehiculo.color = color

coche1 = Coche()
coche2 = Coche()
coche3 = Coche()

motocicleta = Motocicleta()


cambiar_color(coche1, "rojo")
cambiar_color(coche2, "azul")
cambiar_color(coche3, "blanco")

cambiar_color(motocicleta, "negro")

print(coche1.color)
print(coche2.color)
print(coche3.color)
print(motocicleta.color)