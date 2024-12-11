# Funcion zip

nombre_usuario = ["Ema", "Prowler", "Hermano"]
contrasenia = ["123", "abc", "contra"]
fecha_inicio_sesion = ["2020-01-01", "2020-02-01", "2020-03-01"]

#usuarios = list(zip(nombre_usuario, contrasenia)) #Convertido a lista
#usuarios = dict(zip(nombre_usuario, contrasenia)) #Convertido a diccionario
usuarios = list(zip(nombre_usuario, contrasenia, fecha_inicio_sesion)) # con tres elementos iterables

#print(type(usuarios))

#print(usuarios)


#for i in usuarios:
#    print(i)

#for key, value in usuarios.items():
#    print(key + ' : ' + value)

for i in usuarios:
    print(i)