# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def suma(num1, num2):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{num1+num2}')  # Press Ctrl+F8 to toggle the breakpoint.

def resta(num1, num2):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{num1-num2}')  # Press Ctrl+F8 to toggle the breakpoint.

def division(num1, num2):
    # Use a breakpoint in the code line below to debug your script.
    print(f' Cociente:{num1/num2}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(f' Resto:{num1%num2}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Elige una opcion:')
    suma(1,3)
    resta(3,2)
    division(5,2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
