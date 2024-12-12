# Hilos daemon

# los hilos daemon son hilos que se ejecutan en segundo plano
#y no son importantes para su programa
# se utilizan para tareas en segundo plano

import threading
import time


def tiempo():
    print()
    print()
    contador = 0
    while True:
        time.sleep(1)
        contador += 1
        print(contador, 'segundos')

x = threading.Thread(target=tiempo, daemon=True)
#x.setDaemon(False)
x.start()

print(x.isDaemon())

entrada = input('Deseas Salir?')