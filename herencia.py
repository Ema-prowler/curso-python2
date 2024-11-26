# Herencia
#---------

class Animal:

    vivo = True

    def comer(self):
        print("Esta comiendo")

    def dormir(self):
        print("Esta durmiendo")


class Conejo(Animal):
    def correr(self):
        print("Corriendo")

class Pez(Animal):
    def nadar(self):
        print("Nadando")

class Halcon(Animal):
    def volar(self):
        print("Volando")


conejo = Conejo()  # creamos una variable y un objeto que seria "Conejo()" los objetos tienen esta sintaxis
pez = Pez()
halcon = Halcon()


#print(conejo.vivo)
#halcon.dormir()
#pez.comer()
pez.nadar()
conejo.correr()