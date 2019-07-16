"""Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N,
y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original.
Escribir también un programa para verificar el comportamiento de la misma. Hacer tres versiones de la función, para
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter"""

"""def filtrar_palabras(n,fr):   FORMA A
    x=fr.split()
    aux=[]
    for i in range(len(x)):
        if(len(x[i])>=n):
            aux.append(x[i])
    return aux"""

"""def filtrar_palabras(n,fr):
    x=fr.split()
    aux=[x[i] for i in range(len(x)) if(len(x[i])>=n)]
    return aux"""

def filtrar_palabras(n,fr):
    x=fr.split()
    aux=[]
    ss=list(filter(lambda x: len(x)>=n, x))
    return ss
    
    
n=int(input("Numero de caracteres: "))
fr=input("Cadena: ")
func=filtrar_palabras(n,fr)

print("Las palabras formadas por mas de {} caracteres de su oracion son:\n".format(n))
for i in range (len(func)):
    print(func[i])