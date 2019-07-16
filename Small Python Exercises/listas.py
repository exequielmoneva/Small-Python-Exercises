"""Crear una lista con los cuadrados de los numeros entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los ultimos 10 valores
de la lista."""
import random


n=int(input("Ingrese el maximo: "))
lista=[]

lista=[(i+1)**2 for i in range(n)]

if(n<=10):
    for i in range(n-1,-1,-1):
        print(lista[i])
else:
    for i in range(10,-1,-1):
        if(i>0):
            print(lista[i])
