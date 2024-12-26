# Messagebox
from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title='Hola MUNDo', message= 'VIRUSS')
    #while True:
        #messagebox.showwarning(title='PELIGRO', message='TE METI UN VIRUS')
    #messagebox.showerror(title='ERROR', message='Tienes un ERROR')

    #messagebox.askokcancel(title='PELIGRO', message='TE METI UN VIRUS')
    #if (messagebox.askretrycancel(title='PELIGRO', message='TE METI UN VIRUS')):
    #    print('intenta de nuevo noob')
    #else:
    #     print('no intenta de nuevo')

    #messagebox.askyesno(title='PELIGRO', message='TE METI UN VIRUS')
    #pregunta =messagebox.askquestion(title='Pregunta', message='Te gusta el helado ?')
    #if (pregunta == 'yes'):
    #    print('te gusta el helado')
    #else:
    #    print('no te gusta el helado')
    #var = (messagebox.askyesnocancel(title='Advertencia!', message='Estas seguro ?'))
    #print(var)

    messagebox.askyesnocancel(title='Advertencia!', message='Estas seguro ?',icon='warning')

window = Tk()

button = Button(window,
                text='Click me',
                command=click)
button.pack()








window.mainloop()