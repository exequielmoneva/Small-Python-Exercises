"""Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas"""

def suma(a,b):
    if b==0:
        return 0
    else:
        return a + (suma(a,b-1))
        


a=int(input("Primer numero: "))
b=int(input("Segundo numero: "))
func=suma(a,b)

print("La multiplicacion de {} por {} da como resultado {}".format(a,b,func))