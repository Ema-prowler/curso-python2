#   Widget de entrada

from tkinter import *


def enviar():
    nombre_usuario = entrada.get()
    print('hola',nombre_usuario)
    entrada.config(state=DISABLED)

def reset():
    entrada.delete(0, END)

def eliminar():
    entrada.delete( len(entrada.get()) -1, END)


window = Tk()

entrada = Entry(window, font=('Arial', 50), fg='red', bg='#000') #show='*' para ocultar caracteres
entrada.insert(0, 'Hola')
entrada.pack(side=LEFT)  # posicionar entrada a la izquierda

boton_enviar = Button(window, text='Enviar', command=enviar)
boton_enviar.pack(side=RIGHT)  # posicionar boton a la derecha

boton_resetear = Button(window, text='Reset', command=reset)
boton_resetear.pack(side=RIGHT)  # posicionar boton a la derecha


boton_eliminar = Button(window, text='Eliminar', command=eliminar)
boton_eliminar.pack(side=RIGHT)  # posicionar boton a la derecha


window.mainloop()
