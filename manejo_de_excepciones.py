# manejo de excepciones

# una excepcion es un evento detectado durante la ejecución
# de un programa que interrumpe la ejecucion del programa.

try:
    numerador = int(input("Ingrese un numero: "))
    denominador = int(input("Ingrese otro numero: "))
    resultado = numerador / denominador
except ZeroDivisionError as e:
    print(e)
    print("No se puede dividir por cero")
except ValueError as e:
    print(e)
    print("Por favor ingrese solo numeros")
except Exception as e:
    print(e)
    print("Algo salio mal")
else:
    print(resultado)
finally:
    print("Esto siempre se ejecuta")
