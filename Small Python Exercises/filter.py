"""Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma.
Ejemplo, dada la cadena El número de teléfono es 4356-7890
extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas"""

def ext(fr,n,u): #FORMA A
    aux=fr[n:(n+u)]
    return aux

"""def ext(fr,n,u):
    zen=list(fr)
    z=n
    aux=[]
    for i in range(n+u):
        if(z<(n+u)):
            aux.append(zen[z])
        z+=1
    aux="".join(aux)
    return aux
"""
fr=input("Ingrese cadena: ")
n=int(input("Ingrese posicion: "))
u=int(input("Ingrese cantidad de caracteres: "))
func=ext(fr,n,u)
 
print(func)