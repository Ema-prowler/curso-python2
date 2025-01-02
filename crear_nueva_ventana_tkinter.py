# Crear nueva ventana

from tkinter import *

def crear_ventana():
    new_window = Tk()


    window.destroy()


window = Tk()

Button(window,text='Crear nueva ventana',command=crear_ventana).pack()



window.mainloop()