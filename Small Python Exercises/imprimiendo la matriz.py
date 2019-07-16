"""permita verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada función:
a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Intercambiar una fila por una columna, cuyos números se reciben como parámetro.
f. Transponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
g. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.
h. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número
se recibe como parámetro.
i. Determinar si la matriz es simétrica con respecto a su diagonal principal.
j. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
k. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas."""
#FORMO UNA LISTA PARA ORDENAR Y DESPUES RELLENAR CON LOS VALORES EN ORDEN
def relleno(n):
    tempo=[]
    for i in range(n*n):
        te=int(input("Ingrese un valor: "))
        tempo.append(te)
    return tempo
#ORDENO LA LISTA CON REBANDAS
def puntob(tempo,n):
    x=0
    u=0
    fin=[]
    for a in range (n*n-n):   
        t=tempo[x:n+u]
    
        t.sort()
        fin.append(t)
    
        x+=n
        u+=n
    return fin
#IMPRIMO EN FORMA DE MATRIZ
def imprimo(orden):
    filas=n
    columnas=n
    for f in range (filas):
        for c in range(columnas):
            print("%3d"%orden[f][c],end="")
        print()
#CAMBIO FILAS DE LUGAR
def cambiofilas(orden):
    a=int(input("fila: "))
    while(a<=0 or a>n):
        a=int(input("Valor invalido. Por favor, intente otra vez.\n"))
    a-=1

    b=int(input("Otra fila: "))
    while(b<=0 or b>n):
        b=int(input("Valor invalido. Por favor, intente otra vez.\n"))
    b-=1
    columnas=n
    for c in range (columnas):
        aux=orden[a][c]
        orden[a][c]=orden[b][c]
        orden[b][c]=aux
#CAMBIO COLUMNAS DE LUGAR
def cambiocolumnas(orden):
    a=int(input("Columna: "))
    while(a<=0 or a>n):
        a=int(input("Valor invalido. Por favor, intente otra vez.\n"))
    a-=1

    b=int(input("Otra columna: "))
    while(b<=0 or b>n):
        b=int(input("Valor invalido. Por favor, intente otra vez.\n"))
    b-=1
    filas=n

    for f in range(filas):
        aux=orden[f][a]
        orden[f][a]=orden[f][b]
        orden[f][b]=aux
#CAMBIO DE LUGAR UNA FILA CON UNA COLUMNA
def columnayfila(orden):
    a=int(input("fila: "))
    while(a<=0 or a>n):
        a=int(input("Valor invalido. Por favor, intente otra vez.\n"))
    a-=1

    b=int(input("Columna: "))
    while(b<=0 or b>n):
        b=int(input("Valor invalido. Por favor, intente otra vez.\n"))
    b-=1
    columnas=n
    f=0
    for c in range (columnas):
        aux=orden[a][c]
        orden[a][c]=orden[c][b]
        orden[c][b]=aux
    

#INGRESO EL TAMAÑO DE LA MATRIZ POR TECLADO
n=int(input("tamaño matriz: "))
#LLAMO A LAS FUNCIONES
tempo=relleno(n)
orden=puntob(tempo,n)
imprimir=imprimo(orden)
print()#DEJO UN ESPACIO ENTRE LAS IMPRESIONES PARA QUE NO QUEDE TODO PEGADO
"""cfilas=cambiofilas(orden)
imprimir=imprimo(orden)
ccolumnas=cambiocolumnas(orden)
imprimir=imprimo(orden)
puntoE=columnayfila(orden)
imprimir=imprimo(orden)
Transponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)"""

