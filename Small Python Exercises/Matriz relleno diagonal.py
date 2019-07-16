def mat(filas,columnas):
    matriz=[[0] * columnas for i in range(filas)]
    cont=1
    tx=0
    aux=0
    while(columnas>0):
        matriz[tx][columnas-1]=cont
        cont+=2
        tx+=1
        columnas-=1
    
    """for f in range (filas):
        for c in range(columnas):
            if(f==c):
                matriz[f][c]=cont
                cont+=2
      """  
    return matriz


n=int(input("Tamaño de matriz: "))
filas=n
columnas=n
func=mat(filas,columnas)
for f in range (filas):
    for c in range(columnas):
        print("%3d"%func[f][c],end=" ")
    print()