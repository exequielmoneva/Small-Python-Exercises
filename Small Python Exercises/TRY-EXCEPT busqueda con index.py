"""El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda."""
import random
cont=0
lista=[int(input("ingrese un valor: ")) for i in range (10)]

while(cont<3):
    try:
        n=int(input("Ingrese numero entero: "))
        a=lista.index(n,0,100)
        print("La posicion es {}" .format(a))
        
    except ValueError:
        print("Numero no encontrado")
        cont+=1
    