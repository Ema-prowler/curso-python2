# Mover imagenes con teclas
from modulo_random import mi_lista


#def move_up(event):
    #label.place(x=label.winfo_x(), y=label.winfo_y()-10)

#def move_down(event):
    #label.place(x=label.winfo_x(), y=label.winfo_y()+10)

#def move_left(event):
    #label.place(x=label.winfo_x()-10, y=label.winfo_y())

#def move_right(event):
    #label.place(x=label.winfo_x()+10, y=label.winfo_y())


def move_up(event):
    canvas.move(miImagen,0,-10)

def move_down(event):
    canvas.move(miImagen,0,10)

def move_left(event):
    canvas.move(miImagen,-10,0)

def move_right(event):
    canvas.move(miImagen,10,0)

from tkinter import *

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)


canvas = Canvas(window,width=500,height=500)
canvas.pack()

imagen = PhotoImage(file='resources/media/logopython.png')
miImagen = canvas.create_image(0,0,image=imagen,anchor=NW)

#label = Label(window, image=imagen)
#label.place(x=0, y=0)

window.mainloop()