"""Escribir una función que devuelva la cantidad de dígitos de un número entero, sin utilizar cadenas de caracteres"""

def rec(x):

    if x < 9:
        return 1
    else:
        return 1+(rec(x/10))   
     

n=int(input("Ingrese un numero: "))
res=0
func=rec(n)

print("El numero tiene {} digitos".format(func))