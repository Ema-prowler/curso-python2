#Herencia multinivel
#-------------------

class Organismo:
    vivo = True

class Animal(Organismo):
    def comer(self):
        print("Este animal esta comiendo")

class Gatos(Animal):
    def mauyar(self):
        print("Este gato esta mauyando...") #aqui puedes usar return para no devolver el valor None

gato = Gatos()
#print(gato.vivo)
#gato.comer()
#gato.mauyar()

#2 metodos en una linea
#print("-------------------------------")
#print(gato.vivo, end=" | ")
#gato.comer(), gato.mauyar()
print("-------------------------------")
#en una linea formateada
print(f"{gato.vivo}, {gato.comer()}, {gato.mauyar()}")
#Utiliza return en los metodos dentro de las clases para no devolver El valor NONE