"""Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro de otra cadena,
sin diferenciar mayúsculas y minúsculas.
Tener en cuenta que los caracteres de la subcadena no necesariamente deben estar en forma consecutiva dentro de la cadena,
pero sí respetando el orden de los mismos."""

cad=input("Ingrese la cadena: ")
cad=cad.lower()
p=input("Ingrese la palabra a buscar: ")
n=list(p.lower())
pos=0
w=""
i=0
while (pos!=len(cad)):
    res=cad.find(n[i],pos)
    if(res==-1):
        break
    else:
        w+=cad[res]
        pos=res
    if(i<len(n)-1):
        i+=1
    else:
        i=0
if(len(w)<len(n)):
    print("La palabra solicitada no se encuentra en la cadena.")
if(len(w)%len(n)==0):
    print("Se encontro la palabra {} veces en el texto".format(len(w)//len(n)))