"""Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares. Escribir además un programa que permita verificar su
funcionamiento."""
def test(x):
    r=len(x)-1
    
    c=0
    for i in range (len(x)):
        if(x[r]!=x[i]):
            c=-1
        r-=1
    if(c==0):
        return True
    else:
        return False

n=input("Ingrese la cadena: ")
z=list(n.replace(" ",""))
func=test(z)

if (func):
    print("Es capicua")
else:
    
    print("No es capicua")