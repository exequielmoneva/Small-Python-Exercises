"""Desarrollar una función para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de reemplazos realizados. Escribir también un programa para verificar el
comportamiento de la función."""

def rem(fr,x,z):
    fr=fr.split()
    for i in range(len(fr)):
        if(fr[i].lower()==x.lower()):
           fr[i]=z
    return fr

fr=input("Ingrese su cadena: ")
x=input("Palabra: ")
z=input("Palabra a meter: ")
func=rem(fr,x,z)
func=" ".join(func)
print(func)