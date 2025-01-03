# Canvas

from tkinter import *

window = Tk()

# Dimensiones del canvas
canvas_width = 520
canvas_height = 520

# Configuracion del canvas con margen

canvas = Canvas(window, height=canvas_height, width=canvas_width, bg='lightgray')
canvas.pack(pady=10, padx=10)
# Lineas
#canvas.create_line(0,0,500,500,fill='blue',width=5)
#canvas.create_line(0,500,500,0,fill='red',width=5)
#canvas.create_rectangle(50,50,250,250,fill='purple')
#puntos = [250,0,500,500,0,500]
#canvas.create_polygon(puntos,fill='yellow',outline='black',width=5)

#canvas.create_arc(0,0,500,500,fill='green',style=PIESLICE,start=90,extent=180)
# Arcos y círculo central
canvas.create_arc(10, 10, 510, 510, fill='red', extent=180, width=10)  # Parte superior
canvas.create_arc(10, 10, 510, 510, fill='white', extent=180, start=180, width=10)  # Parte inferior
canvas.create_oval(200, 200, 320, 320, fill='white', width=10)  # Centro

canvas.pack(pady=10, padx=10)
window.mainloop()