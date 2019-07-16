"""Ejemplo de ejercicio de parcial.
Rellenar una matriz debajo de su diagonal y desde el codigo,
con el numero de su tamaño y todos los menores hasta el 1"""

n=int(input("Ingrese el tamaño de la matriz: "))
filas=n
columnas=0
aux=n
matriz=[[0]*n for i in range(n)]

for f in range (filas):
    while(columnas<=f):
        matriz[f][columnas]=aux
        columnas+=1
    columnas=0
    aux-=1
    
    
filas=n
columnas=n
for f in range(filas):
    for c in range (columnas):
        print("%3d"%matriz[f][c],end=" ")
    print()
