# Proteccion del punto de entrada if

def main():
    print('Hola')


if __name__ == '__main__': #basicamente esto es un constructor de la programacion en python
    main()                 # Que controla la ejecucion de un script
else:
    print("Este modulo indirectamente")

# Este sentencia permite mas flexibilidad en la ejecucion de programas
# pueden ejecutarse como proramas independientes o pueden ser importados y utilizados por otros modulos
