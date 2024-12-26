# Listbox

from tkinter import *

def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print('Su orden es:')
    #print(listbox.get(listbox.curselection()))
    for index in food:
        print(index)



def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    #listbox.delete(listbox.curselection())

    for index in reversed(listbox.curselection()):
        listbox.delete(index)



    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('Arial', 30),
                  width=20,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Pizza turca")
listbox.insert(1, "Pizza napolitana")
listbox.insert(1, "Pizza caprese")
listbox.insert(1, "Pizza mozzarella")
listbox.insert(1, "Pizza con champiñones")

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()




submitButton = Button(window, text='Enviar', command=submit)
submitButton.pack()

addButton = Button(window, text='Agregar', command=add)
addButton.pack()

deleteButton = Button(window, text='Eliminar', command=delete)
deleteButton.pack()



window.mainloop()
