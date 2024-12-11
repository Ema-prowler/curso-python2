# Funcion filter

amigos = [("Alu", 20),
          ("Ema", 19),
          ("Cine", 18),
          ("Anukis", 17),
          ("Isaias", 16),
          ("Pepino", 13)]

edad = lambda dato: dato[1] >= 18

amigos_bebida = list(filter(edad, amigos))

for i in amigos_bebida:
    print(i)