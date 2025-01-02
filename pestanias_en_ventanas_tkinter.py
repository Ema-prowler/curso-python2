# Pestanas en ventanas

from tkinter import *
from tkinter import ttk

from PIL.ImageOps import expand

window = Tk()

notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill='both')

tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.add(tab3, text='Tab 3')

Label(tab1, text='Pestania #1',width=50,height=25).pack()
Label(tab2, text='Pestania #2',width=50,height=25).pack()
Label(tab3, text='Pestania #3',width=50,height=25).pack()



window.mainloop()
