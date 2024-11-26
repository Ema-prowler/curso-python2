#Herencia multiple
#-----------------

class Presa:
    def huir(self):
        print("Este animal esta huyendo")

class Depredador:
    def cazar(self):
        print("Este animal esta cazando")

class Conejo(Presa):
    pass

class Halcon(Depredador):
    pass

class Pez(Presa, Depredador):
    pass
#Creando objetos para cada clase
conejo = Conejo()
halcon = Halcon()
pez = Pez()

#conejo.huir()
#halcon.cazar()
pez.huir()
pez.cazar()