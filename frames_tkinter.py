# Frames

from tkinter import *

window = Tk()

marco = Frame(window,bg='pink',bd=5,relief=SUNKEN)
marco.pack(side=LEFT)
#marco.place(x=100,y=100)

Button(marco,text='W', font=('Consolas', 25), width=3).pack(side=TOP)
Button(marco,text='A', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(marco,text='S', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(marco,text='D', font=('Consolas', 25), width=3).pack(side=LEFT)



window.mainloop()