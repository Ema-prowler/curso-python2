# Compresiones de listas

#ejemplo 1

#cuadrado = []

#for i in range(1,11):
#    cuadrado.append(i*i)
#print(cuadrado)

#cuadrado = [i*i for i in range(1,11)] # forma en una sola linea
#print(cuadrado)

estudiantes = [100,90,80,70,60,50,40,30,0]

#estudiantes_aprobados = list(filter(lambda x: x >= 60, estudiantes))

#estudiantes_aprobados = [i for i in estudiantes if i >= 60] # con condicion y compresion de listas

estudiantes_aprobados = [i if i >= 60 else "-" for i in estudiantes] # con compresion de listas y condicion

print(estudiantes_aprobados)