# Compresiones de diccionarios

# diccionario = {lkey: expresion for (key, value) in iterable}

#ciudades_en_F = {'New york': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

#ciudades_en_C = {key: round((value-32)*(5/9)) for (key, value) in ciudades_en_F.items()}

#print(ciudades_en_C)
#-------------------------------------------------------------------------------

# Segundo ejemplo

#clima = {'New York': 'Nieve', 'Boston': 'Soleado', 'Los angeles': 'Soleado', 'Chicago': 'Nublado'}

#clima_soleado = {key: value for (key, value) in clima.items() if value == 'Soleado'}

#print(clima_soleado)

#-------------------------------------------------------------------------------

# Tercer ejemplo

#clima = {'New york': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#clima2 = {key: ("CALOR" if value >= 40 else "FRIO") for (key, value) in clima.items()}
#print(clima2)

#-------------------------------------------------------------------------------

# Cuarto ejemplo

def check_temp(value):
    if value >= 70:
        return "CALOR"
    elif 60 >= value >= 40:
        return "NORMAL"
    else:
        return "FRIO"


ciudades = {'New york': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

clima = {key: check_temp(value) for (key, value) in ciudades.items()}
print(clima)