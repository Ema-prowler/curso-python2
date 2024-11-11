# Funciones

def saludo(primer_nombre,apellido, edad):  # hay que tener un conjunto coincindente llamado parametro o paramteros.
    # La variable nombre es temporal y solo puede ser usada dentro de la funcion (es local)
    print("Hola " + primer_nombre + " " + apellido)
    print("Tienes " + str(edad) + " años")
    print("Que tengas un buen dia!")

#nombre = "ema"
nombre = input("Ingresa tu nombre: ")

#saludo("ema")   # Llamamos a la funcion | argumento a una funcion
saludo(nombre, "prowler", 27)

# Una funcion es un bloque de codigo que se ejecuta solo cuando se lo llama
