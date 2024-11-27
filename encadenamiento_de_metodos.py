# Encadenamiento de metodos

class Coche:
    def encender(self):
        print("Has arrancado el motor")
        return self

    def conducir(self):
        print("Estas conduciendo el coche")
        return self

    def frenar(self):
        print("Estas pisando los frenos")
        return self

    def apagar(self):
        print("Has apagado el motor")
        return self


coche = Coche()

#coche.encender().conducir()

#coche.frenar().apagar()

coche.encender().conducir().frenar().apagar() # Encadenamiento de metodos

# forma en teoria mas ordenada

#(coche.encender()
# .conducir()
# .frenar()
# .apagar())