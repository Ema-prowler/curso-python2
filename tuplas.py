# Tuplas

# las tuplas son colecciones ordenadas e inmutables.
# Las tuplas no se pueden cambiar o modificar una vez creadas.

estudiantes = ("ema",27,"M","cat",27,"F")

print(estudiantes.count(27))

print(estudiantes.index("M"))

print("Separador")

for x in estudiantes:
    print(x)

if "ema" in estudiantes:
    print("ema esta aqui")
else:
    print("ema no esta aqui")