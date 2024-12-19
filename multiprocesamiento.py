# multiprocesamiento

from multiprocessing import Process, cpu_count

import time


def contador(num):
    cont = 0
    while cont < num:
        cont += 1



def main():

    iniciar = time.perf_counter()

    a = Process(target=contador, args=(200000000,))     # este seria un hilo
    b = Process(target=contador, args=(200000000,))     # este seria otro hilo
    c = Process(target=contador, args=(200000000,))    # este seria otro hilo
    d = Process(target=contador, args=(200000000,))    # este seria otro hilo
    e = Process(target=contador, args=(100000000,))    # este seria otro hilo
    f = Process(target=contador, args=(100000000,))    # este seria otro hilo
    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()

    fin = time.perf_counter()
    tiempo = fin - iniciar
    print('finalizo: ', tiempo, 'segundos')
    print(cpu_count())


if __name__ == '__main__':
    main()