#  Funcion reduce
# reduce(funcion, iterable)

import functools
from math import factorial

#letras = ["H","O","L","A"]

#palabra = functools.reduce(lambda x,y: x + y ,letras)
#print(palabra)

factorial = [5,4,3,2,1]

resultado = functools.reduce(lambda x,y: x*y, factorial)
print(resultado)