# Modulo threading

import threading
import time

def desayunar():
    print('Iniciando desayunar...')
    time.sleep(3)
    print('Finalizado...')

def tomar_cafe():
    print('Iniciando tomar cafe...')
    time.sleep(4)
    print('Finalizado...')

def estudiar():
    print('Iniciando estudiar...')
    time.sleep(5)
    print('Finalizado...')


inicio = time.perf_counter()

x = threading.Thread(target=desayunar, args=())
x.start()

y = threading.Thread(target=tomar_cafe, args=())
y.start()

z = threading.Thread(target=estudiar, args=())
z.start()

x.join()
y.join()
z.join()

#desayunar()
#tomar_cafe()
#estudiar()

print(threading.active_count())
print(threading.enumerate())

fin = time.perf_counter()

tiempo = fin - inicio
print(tiempo)