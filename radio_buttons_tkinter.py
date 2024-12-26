from tkinter import *
from PIL import Image, ImageTk

comida = ['Pizza', 'Hamburguesa', 'Hot Dog']


def orden():
    if ( x.get() == 0):
        print('has ordenado una pizza')
    elif ( x.get() == 1):
        print('haz ordenado una Hamburguesa')
    elif ( x.get() == 2):
        print('has ordenado un Hot Dog')
    else:
        print('no has seleccionado ninguna opción')



ventana = Tk()

# Cargar y redimensionar imágenes
def redimensionar_imagen(ruta_imagen, tamano_objetivo):
    img = Image.open(ruta_imagen)
    img = img.resize(tamano_objetivo, Image.LANCZOS)  # Usar filtro LANCZOS para redimensionar con alta calidad
    return ImageTk.PhotoImage(img)

# Definir tamaño objetivo de las imágenes (por ejemplo, 100x100 píxeles)
tamano_objetivo = (100, 100) 

imagen_pizza = redimensionar_imagen('D:\\Programacion\\curso-python\\resources\\media\\pizza.png', tamano_objetivo)
imagen_hamburguesa = redimensionar_imagen('D:\\Programacion\\curso-python\\resources\\media\\hamburguesa.png', tamano_objetivo)
imagen_hotdog = redimensionar_imagen('D:\\Programacion\\curso-python\\resources\\media\\HotDog.png', tamano_objetivo)
imagenes_comida = [imagen_pizza, imagen_hamburguesa, imagen_hotdog]

x = IntVar()

for indice in range(len(comida)):
    boton_radio = Radiobutton(ventana,
                              text=comida[indice],
                              variable=x,
                              value=indice,
                              padx=25,
                              pady=25,
                              font=('Arial', 50),
                              image=imagenes_comida[indice],
                              compound='left',
                              indicatoron=0,
                              width=500,
                              command=orden)
    boton_radio.pack(anchor=W)

ventana.mainloop()