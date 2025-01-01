# Menu
from tkinter import *

def abrirArchivo():
    print('Abrirendo archivo')

def guardarArchivo():
    print('Guardando archivo')

def cortar():
    print('Cortando')

def copiar():
    print('Copiando')

def pegar():
    print('Pegando')


window = Tk()

openImage = PhotoImage(file='resources/media/abrir.png')
saveImage = PhotoImage(file='resources/media/guardar.png')
exitImage = PhotoImage(file='resources/media/salir.png')



menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=('MV Boli', 15))
menubar.add_cascade(label='Archivos', menu=fileMenu)
fileMenu.add_command(label='Abrir', command=abrirArchivo, image=openImage,  compound='left')
fileMenu.add_command(label='Guardar', command=guardarArchivo, image=saveImage,  compound='left')
fileMenu.add_separator()
fileMenu.add_command(label='Salir', command=quit, image=exitImage,  compound='left')

editMenu = Menu(menubar, tearoff=0,font=('MV Boli', 15))
menubar.add_cascade(label='Editar', menu=editMenu)
editMenu.add_command(label='Cortar', command=cortar)
editMenu.add_command(label='Copiar', command=copiar)
editMenu.add_command(label='Pegar', command=pegar)


window.mainloop()