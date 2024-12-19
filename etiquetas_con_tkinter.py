#   Etiquetas con tkinter

from tkinter import *

window = Tk()

#window.geometry('500x500')
window.config(bg='black')
label = Label(window,
              text='Hola, quieres aprender a programar?',
              font=('Arial', 40, 'bold'),
              fg='white',
              bg='black',
              relief='raised',
              bd=10,
              padx=10,
              pady=10)
label.pack(padx=150, pady=150)
#label.place(x=0, y=0)  # posicion


window.mainloop()
