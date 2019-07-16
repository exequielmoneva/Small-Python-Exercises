"""Realizar una función que devuelva el resto de dos números enteros, utilizando restas sucesivas"""

def suma(a,b):
    if a<b:
        return a
    else:
        return  (suma(a-b,b))
        


a=int(input("Primer numero: "))
b=int(input("Segundo numero: "))
func=suma(a,b)

print("El modulo entre {} y {} da como resultado {}".format(a,b,func))