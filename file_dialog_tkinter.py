# File Dialog

from tkinter import *
from tkinter import filedialog

def abrirArchivo():
    filepath = filedialog.askopenfilename(title='Abrir archivo',
                                          filetypes=(('archivo de texto','*.txt'),
                                                     ('Todos los archivos','*.*')))# initialdir='C:/Users/User/Desktop', como ejemplo de ruta por defecto
    archivo = open(filepath, 'r')
    print(archivo.read())


window = Tk()


boton = Button(window,text='Abrir', command=abrirArchivo)
boton.pack()



window.mainloop()