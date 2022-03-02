def suma():
    print(f'Sumar')
    num1 = float(input('Introduce el primer valor: '))
    num2 = float(input('Introduce el segundo valor: '))
    print(f'La suma es: {num1+num2}')

def resta():
    print(f'Restar')
    num1 = float(input('Introduce el primer valor: '))
    num2 = float(input('Introduce el segundo valor: '))
    print(f'La resta es: {num1 - num2}')



def division():
    print('Dividir')
    num1 = float(input('Introduce el primer valor: '))
    num2 = float(input('Introduce el segundo valor: '))
    print(f'La division es: {num1/num2}')

def multiplicacion():
    print('Multiplicar')
    num1 = float(input('Introduce el primer valor: '))
    num2 = float(input('Introduce el segundo valor: '))
    print(f'La multiplicacion es: {num1*num2}')

def elevado():
    print('Elevar')
    num1 = int(input('Valor a elevar '))
    num2 = int(input('Elevar a '))
    num3 = 1
    for value in range(0,num2):
        num3 = num3 *num1
        print(f'{num3}')
    print(f'el resultado es: {num3} ')