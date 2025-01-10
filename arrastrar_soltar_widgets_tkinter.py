# Arrastrar y soltar widgets

from tkinter import *

def arrastrar(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def arrastrat2(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


window = Tk()

label = Label(window, bg='red', width=10,height=5)
label.place(x=0, y=0)

label2 = Label(window, bg='blue', width=10,height=5)
label2.place(x=100, y=100)


label.bind("<Button-1>",arrastrar)
label.bind("<B1-Motion>",arrastrat2)

label2.bind("<Button-1>",arrastrar)
label2.bind("<B1-Motion>",arrastrat2)

window.mainloop()