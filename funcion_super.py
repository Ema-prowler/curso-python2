# Funcion super

class Recntangulo:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

class Cuadrado(Recntangulo):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)

    def area(self):
        return self.alto * self.ancho

class Cubo(Recntangulo):
    def __init__(self, alto, ancho, largo):
        self.largo = largo
        super().__init__(alto, ancho) # la funcion super sirve para llamar a los metodos de la clase padre

    def volumen(self):
        return self.alto * self.ancho * self.largo

cuadrado = Cuadrado(3, 3)
cubo = Cubo(3,3,3)

print(cuadrado.area())
print(cubo.volumen())