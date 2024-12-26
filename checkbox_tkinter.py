#   Checkbox

from tkinter import *

def mostrar():
    if x.get() == 1:
        print('Estas de acuerdo')
    else:
        print('No estas de acuerdo')


window = Tk()

x = IntVar()

python_photo = PhotoImage(file='resources/media/logo.png')


check_button = Checkbutton(window,
                           text='Acepto',
                           variable = x,
                           onvalue  = 1,
                           offvalue = 0,
                           command=mostrar,
                           font=('Arial', 20),
                           fg='red',
                           bg='#000',
                           activeforeground='red',
                           activebackground='#000',
                           padx=25,
                           pady=25,
                           image=python_photo,
                           compound='left')
check_button.pack()




window.mainloop()
