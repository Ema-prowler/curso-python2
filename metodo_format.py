# meteodo format

# el metodo format es un metodo disponible para las cadenas de texto.
# es opcional y brinda a los usuarios un mayor control al mostrar los resultados.

str_1 = "todo"
str_2 = "amigos"


#print("esto es todo amigos")

#print("esto es " + str_1 + " " + str_2)   #forma 1
#print("esto es {} {}".format("todo", "amigos"))  # forma 2 colocando las cadenas de caracteres
print("esto es {} {}".format(str_1, str_2))  # forma 3 usando metodo format
#el campo de formato funciona en orden de aparicion
# las variables dentro del metodo format en este caso : str_1 y str_2 tienen un indice
# Por ejemplo: print("esto es {1} {0}".format(str_1, str_2) #str_1 tiene indice 0 y str_2 tiene indice 1
print("esto es {str_1} {str_2}".format(str_1= "todo", str_2= "amigos")) #aqui no se puede usar el indice
print("esto es {str_1} {str_2}".format(str_1= str_1, str_2=str_2))  # mandandole una variable a las claves


texto = "esto es {} {}"
#print(texto.format(str_1, str_2)) #este es otra forma de usar el metodo format

nombre = "ema"
#print("hola, mi nombre es {} ".format(nombre))
#print("hola, mi nombre es {:10}. Mucho gusto :D ".format(nombre)) #coloca 10 espacios en blanco
#print("hola, mi nombre es {:<10}. Mucho gusto :D ".format(nombre)) #coloca 10 espacios en blanco a la izquierda
#print("hola, mi nombre es {:>10}. Mucho gusto :D ".format(nombre)) #coloca 10 espacios en blanco a la derecha
#print("hola, mi nombre es {:^10}. Mucho gusto :D ".format(nombre)) # centrar texto en 10 espacios 5 a la derecha y 5 a la izquierda
# ^ acento circunflejo
numero = 3.14159
numero2 = 1000
print("El numero PI es: {:.2f}".format(numero)) # .2f singnifica 2 fracciones despues del punto
# si quieres usar el metodo format y quieres hacer algo con el, especifico siempre debes colocar (:)
print("El numero es: {:b}".format(numero2)) # b significa binario mostrara el numero en binario
print("El numero es: {:o}".format(numero2)) # o significa octal mostrara el numero en octal
print("El numero PI es: {:x}".format(numero2)) # x significa hexadecimal mostrara el numero en hexadecimal
print("El numero PI es: {:X}".format(numero2)) # X significa hexadecimal mayusculas mostrara el numero en hexadecimal
print("El numero PI es: {:e}".format(numero2)) # e significa exponencial mostrara el numero en exponencial o notación científica
print("El numero PI es: {:E}".format(numero2)) # E significa exponencial mayusculas mostrara el numero en exponencial o notación científica

