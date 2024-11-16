# Variables de Clase
#-------------------

from automovil import Auto

auto_1 = Auto("Ford","Mustang",2000,"Azul")
auto_2 = Auto("Chevrolet","Corvette",2010,"Rojo")

#Auto.ruedas = 2 # se cambia el valor de la variable de clase
# esto afectara a todas las instancias de la clase

# Tambien puedes cambiar las ruedas de un auto en especifico:

auto_1.ruedas = 2

print(Auto.ruedas) # forma alternativa de acceder a la variable de clase

# Por ejemplo:

print(auto_1.ruedas) # muestra que el auto tiene 2 ruedas
print(auto_2.ruedas) # muestra que el auto tiene 2 ruedas
