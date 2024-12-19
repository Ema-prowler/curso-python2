#   Crear boton con tkinter

from tkinter import *

def click():
    print('Hiciste click en el boton')


window = Tk()

imagen = PhotoImage(file='resources/media/click.png')

boton = Button(window,
               text='Haz click',
               command=click,
               font=('Arial', 20, 'bold'),
               fg='white',
               bg='black',
               activeforeground='white',
               activebackground='black',
               state=('active'),
               relief='raised',
               bd=10,
               padx=10,
               pady=10,
               image=imagen,
               compound='bottom')
boton.pack()

window.mainloop()
