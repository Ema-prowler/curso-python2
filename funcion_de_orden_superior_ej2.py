# Funcion de orden superior
# Ejemplo 2

def divisor(x):
    def dividendo(y):
        return y / x
    return dividendo

divide = divisor(2)
print(divide(10))