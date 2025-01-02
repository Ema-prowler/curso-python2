# Grid

from tkinter import *

window = Tk()

tituloLabel = Label(window, text='Ingrese su Informacion', font=('Arial',25)).grid(row=0, column=0,columnspan=2)


nombreLabel = Label(window, text='Nombre:',width=20,bg='red').grid(row=1, column=0)
nombreEntry = Entry(window).grid(row=1, column=1)

apellidoLabel = Label(window, text='Apellido:',bg='green').grid(row=2, column=0)
apellidoEntry = Entry(window).grid(row=2, column=1)

emailLabel = Label(window, text='Email:',bg='blue',width=40).grid(row=3, column=0)
emailEntry = Entry(window).grid(row=3, column=1)

enviarButton = Button(window, text="Enviar").grid(row=4, column=0, columnspan=2)

window.mainloop()
