#  Animaciones múltiples con Tkinter

from tkinter import *
from ball import *
import time

WIDTH = 500
HEIGHT = 500


window = Tk()


canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,120,8,2,"orange")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()