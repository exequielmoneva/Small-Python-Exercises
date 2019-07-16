n=int(input("tamaño: "))
matriz=[[0]*n for i in range (n)]
filas=n
columnas=n
cont=1
for f in range(filas,-1,-1):
    if(f==0):
        cont=1
    for c in range(columnas,-1,-1):
        matriz[f-1][c-1]=cont
    cont+=cont
    
    
    

for f in range(filas):
    for c in range(columnas):
        print("%3d"%matriz[f][c],end=" " )
    print()
