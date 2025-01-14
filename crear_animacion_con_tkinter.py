#  Crear animación con Tkinter


from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xvelocity = 1.5
yvelocity = 1.5


window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg='#000')
canvas.pack()

photo_image = PhotoImage(file='resources/media/HermesVolador.png')
my_image = canvas.create_image(0,0, image=photo_image, anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()


while True:
    coordenadas = canvas.coords(my_image)
    print(coordenadas)
    if (coordenadas[0]>=WIDTH - image_width or coordenadas [0] < 0):
        xvelocity = -xvelocity
    if (coordenadas[1]>=HEIGHT - image_height or coordenadas [1] < 0):
        yvelocity = -yvelocity
    canvas.move(my_image, xvelocity, yvelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()