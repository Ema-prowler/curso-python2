# Scale
from tkinter import *

def submit():
    print('La temperatura es: ' + str(scale.get()) + ' grados')


window = Tk()

hotImage = PhotoImage(file='D:\\Programacion\\curso-python\\resources\\media\\Calor.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=('Arial', 20),
              tickinterval=10,
              #showvalue=0,
               resolution=5,
              troughcolor='#ff6600',
              fg='#ff1c00',
              bg='#111111',)

scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()


coldImage = PhotoImage(file='D:\\Programacion\\curso-python\\resources\\media\\Frio.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()



boton = Button(window,
               text='Enviar',
               command=submit)
boton.pack()




window.mainloop()