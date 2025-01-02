# Barra de progreso

from tkinter import *
from tkinter.ttk import *
import time

def start():
    gb = 100
    download = 0
    speed = 1
    while (download < gb):
        time.sleep(0.05)
        bar['value'] += (speed/gb)*100
        download += speed
        porcentaje.set(str(int((download/gb)*100))+'%')
        texto.set(str(download)+"/"+str(gb)+" GB completado")
        window.update_idletasks()



window = Tk()

porcentaje = StringVar()
texto = StringVar()


bar = Progressbar(window, orient='horizontal', length=300)
bar.pack(pady=10)

textoLabel = Label(window, textvariable=porcentaje).pack()
comLabel = Label(window, textvariable=texto).pack()

boton = Button(window, text='Descargar', command=start).pack()



window.mainloop()
