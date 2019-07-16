"""Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0. Devolver el valor ingresado cuando
éste sea correcto. Escribir también un programa que permita probar el correcto
funcionamiento de la misma."""

try:
    n=list(input('ingrese un numero: '))
    if("." in n):
        n="".join(n)
        n=float(n)
        raise ValueError
    else:
        n="".join(n)
        if(n.isdigit()==True):
            assert n<0
        else:
            raise NameError
    
except AssertionError as e:
    print("El numero ingresado es negativo")
except ValueError:
    print('El numero ingresado no es entero')
except NameError:
    print("eso es una cadena")
    