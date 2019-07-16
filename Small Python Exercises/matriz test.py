def cargar(matriz,u):
        filas=u
        columnas=u
        aux=[]
        d=filas*columnas
        for r in range(d):
                n=int(input("Ingrese un valor: "))
                aux.append(n)
        r=0
        aux.sort()
        for f in range(filas):
                for c in range(columnas):
                        matriz[f][c]=aux[r]
                        r+=1
        return matriz
def impr(mat,filas,columnas):
        for f in range(filas):
                for c in range(columnas):
                        print("%3d"%mat[f][c],end=" ")
                print()


n=int(input("tamaño matriz: "))
filas=n
columnas=n
mat=[[0]*n for i in range(n)]

puntoA=cargar(mat,n)
pr=impr(mat,filas,columnas)
