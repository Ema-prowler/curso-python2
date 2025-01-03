# Eventos de teclado

from tkinter import *

def hacer_algo(event):
    # print('Haz Presionado: ' + event.keysym)
    label.config(text=event.keysym)
window = Tk()

window.bind("<Key>",hacer_algo)

label = Label(window, font=('Helvetica', 100))
label.pack()


window.mainloop()