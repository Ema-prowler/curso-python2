# Ordenar iterables

estudiantes = ("Alu", "Ema", "Cine", "Anukis", "Isaias")
# no se puede ocuopar el metodo sort en una tupla


#estudiantes.sort() #tambien puedes usar reverse=True aqui adentro de la funcion sort
estudiantes2 = sorted(estudiantes, reverse=True) #Convierte la tupla en una lista
#reverse=True ordena de mayor a menor



for i in estudiantes2:
    print(i)

#-----------------