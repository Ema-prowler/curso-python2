# Clases abstractas

from abc import ABC, abstractmethod




class Vehiculo(ABC):
    @abstractmethod # no permites al usuario llamar a este metodo ir
    def ir(self):
        pass
    def detener(self):
        pass

class Coche(Vehiculo):
    def ir(self):
        print("Conduces el Auto")

    def detener(self):
        print("Este coche esta detenido")

class Motocicleta(Vehiculo):
    def ir(self):
        print("Andas en Moto")

    def detener(self):
        print("Esta motocicleta esta detenida")



#vehiculo = Vehiculo()
coche = Coche()
motocicleta = Motocicleta()

#vehiculo.ir()
coche.ir()
motocicleta.ir()

#vehiculo.detener()
coche.detener()
motocicleta.detener()