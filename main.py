import Calculos


if __name__ == '__main__':
    print('1 - Sumar\n2 - Restar')
    opcion= int(input('Elige una opcion: '))
    if opcion==1:
        Calculos.suma()
    if opcion==2:
        Calculos.resta()
    if opcion==3:
        Calculos.division()



