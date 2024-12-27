# Color Chooser

from tkinter import *
from tkinter import colorchooser

def click():
    #color = colorchooser.askcolor()
    #colorHex = color[1]
    #print(colorHex)
    window.config(bg=colorchooser.askcolor()[1])




window = Tk()

window.geometry('420x420')

boton = Button(text='Haz click en mi', command=click)
boton.pack()

window.mainloop()


