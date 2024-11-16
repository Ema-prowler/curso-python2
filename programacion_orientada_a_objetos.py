# Programacion Orientada a Objetos
#----------------------------------


from automovil import Auto

auto_1 = Auto("Ford","Mustang",2000,"Azul")
auto_2 = Auto("Chevrolet","Corvette",2010,"Rojo")

print(auto_1.marca)
print(auto_1.modelo)
print(auto_1.anio)
print(auto_1.color)

auto_1.encendido()
auto_1.apagado()