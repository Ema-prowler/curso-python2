

class Auto:
    #las variables declaradas fuera del constructor se conocen como variables de clase

    ruedas = 4 # esto es una variable de clase
    # Ahora por defecto todos los autos creados tendran 4 ruedas.↓
                                                                #↓
                                                                #↓
    def __init__(self,marca,modelo,anio,color): # funciona como un constructor
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        # las variables declaradas dentro del constructor se conocen como variables de instancia
        # cada objeto puede tener su propios valores unicos asignados a estas variables.

    def encendido(self):
        print("El auto esta encendido")

    def apagado(self):
        print("El auto esta apagado")

