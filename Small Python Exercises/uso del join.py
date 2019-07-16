"""Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante.
Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas"""
def dele(fr,n,u): #FORMA A
    aux=list(fr)
    del aux[n:n+u]
    aux="".join(aux)
    return aux
   
"""def dele(fr,n,u): FORMA B
    aux=list(fr)
    z=n
    for i in range (u):
        
        del(aux[z])
        
    aux="".join(aux)
    return aux
"""
fr=input("Cadena: ")
n=int(input("Posicion: "))
u=int(input("cantidad de caracteres: "))
func=dele(fr,n,u)

print(func)