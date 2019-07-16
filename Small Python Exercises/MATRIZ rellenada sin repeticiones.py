"""Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita. Imprimir la matriz por pantalla."""
import random
n=int(input("Tamaño de la matriz: "))
filas=n
columnas=n
matriz=[]
matriz=[[0]*n for i in range(n)]
aux=[]
num=0
while(len(aux)<n*n):
    num=random.randint(0,(n**2)-1)
    if(num not in aux):
        aux.append(num)
a=0
print(sorted(aux))
for f in range (filas):
    for c in range(columnas):
        matriz[f][c]=aux[a]
        a+=1

for f in range (filas):
    for c in range(columnas):
        print("%3d"%matriz[f][c],end=" ")
    print()
