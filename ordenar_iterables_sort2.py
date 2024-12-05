# Ordenar iterables
estudiantes =(("Alu", "F", 20),
              ("Ema", "A" ,19),
              ("Cine", "D", 18),
              ("Anukis", "B", 17),
              ("Isaias", "C" ,16))


edad = lambda tupla: tupla[2]


#estudiantes.sort(key=edad, reverse=True)
estudiantes2 = sorted(estudiantes, key=edad)

for i in estudiantes2:
    print(i)