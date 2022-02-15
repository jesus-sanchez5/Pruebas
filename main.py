import Calculos


if __name__ == '__main__':
    i = 0
    while i != 1:
        print('1 - Sumar\n2 - Restar\n3 - Division\n4 - Multiplicacion\n\n0 - Salir')
        opcion= int(input('Elige una opcion: '))
        if opcion==1:
            Calculos.suma()
        if opcion==2:
            Calculos.resta()
        if opcion==3:
            Calculos.division()
        if opcion==4:
            Calculos.multiplicacion()
        if opcion==0:
            i=1



