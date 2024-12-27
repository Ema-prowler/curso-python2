# Text Area

from tkinter import *

def enviar():
    input = texto.get('1.0', END)
    print(input)


window = Tk()

texto = Text(window,
             bg='#ffffe0',
             font=('Ink Free', 25,),
             height=8,
             width=20,
             padx=20,
             pady=20,
             fg='red')
texto.pack()


boton = Button(window, text='Enviar', command=enviar)
boton.pack()



window.mainloop()