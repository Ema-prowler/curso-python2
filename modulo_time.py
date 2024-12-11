# Modulo time

import time
from pprint import PrettyPrinter

#print(time.ctime(0)) # 0 es el tiempo de referencia que toma la computadora
#print(time.ctime(1000000))
#print(time.time()) # tiempo transcurrido desde el tiempo de referencia en segundos
#print("SEPARADOR")
#print(time.ctime(time.time()))
#print("SEPARADOR")
#tiempo_actual = time.localtime()
#print(tiempo_actual)

#tiempo_actual = time.localtime()
#tiempo_actual = time.gmtime()
#tiempo = time.strftime("%B %d %y %H:%M:%S", tiempo_actual)
#print(tiempo)


#cadena_tiempo = '14 October, 2024'
#tiempo = time.strptime(cadena_tiempo, '%d %B, %Y')
#print(tiempo)

tiempo_tupla = (2023, 4, 14, 4, 20, 0, 0, 0, 0)
cadena_tiempo = time.asctime(tiempo_tupla)
print(cadena_tiempo)

tiempo_tupla = (2023, 4, 14, 4, 20, 0, 0, 0, 0)
cadena_tiempo = time.mktime(tiempo_tupla)
print(cadena_tiempo)