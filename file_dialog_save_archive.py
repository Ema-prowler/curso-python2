# File Dialog

from tkinter import *
from tkinter import filedialog

# initialdir='C:/Users/User/Desktop', como ejemplo de ruta por defecto


def guardarArchivo():
    archivo = filedialog.asksaveasfile(defaultextension='.txt',
                                       filetypes=(('Archivo de texto','*.txt'),
                                                  ('HTML','html'),
                                                  ('Todos los archivos','.*')))
    if archivo is None:
        return
    archivoTexto = texto.get('1.0', END)
    archivo.write(archivoTexto)
    archivo.close()

window = Tk()

boton = Button(window,text='Guardar', command=guardarArchivo)
boton.pack()

texto = Text(window)
texto.pack()



window.mainloop()