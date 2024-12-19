# Interfaz gráfica de usuario


from tkinter import *

windows = Tk()
windows.geometry('500x500')

windows.title('Aprende a programar')
icono = PhotoImage(file='resources/media/icono.png')
windows.iconphoto(True, icono)

windows.config(bg='black')


windows.mainloop()
