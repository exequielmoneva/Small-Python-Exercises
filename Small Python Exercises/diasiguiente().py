"""Escribir una funcion diasiguiente() que reciba como parámetro una fecha cualquiera expresada por tres enteros (correspondientes al dia, mes y ano) y calcule y
devuelva tres enteros correspondientes el dia siguiente al dado.
Utilizando esta funcion, desarrollar programas que permitan:
a. Sumar N dias a una fecha.
b. Calcular la cantidad de dias existentes entre dos fechas cualesquiera."""
#4 6 9 11
def diasiguiente(dia,mes,ano):
    if(mes==2):
        if(ano%4==0 and ano%100!=0 or ano%400==0):
            if(dia<29):
                dia+=1
            else:
                dia=1
                mes+=1
        else:
            if(dia<28):
                dia+=1
            else:
                dia=1
                mes+=1
    elif(mes==12):
        if(dia<31):
            dia+=1
        else:
            dia=1
            mes=1
            ano+=1
    else:
        if (mes in [4,6,9,11]):
            if (dia<30):
                dia+=1
            else:
                dia=1
                mes+=1
        else:
             if (dia<31):
                dia+=1
             else:
                dia=1
                mes+=1
    return dia, mes, ano

d=int(input("Ingrese dia: "))
m=int(input("Ingrese mes: "))
a=int(input("Ingrese ano: "))

dia,mes,ano=diasiguiente(d,m,a)

print("{}/{}/{}".format(dia,mes,ano))
print("\n")
da=int(input("\nIngrese el primer dia a comparar:"))
ma=int(input("Ingrese el mes :"))
anoa=int(input("Ingrese el ano :"))

db=int(input("Ingrese el segundo dia a comparar:"))
mb=int(input("Ingrese el mes :"))
anob=int(input("Ingrese el ano :"))

may=-1
#1 PARA A MAYOR 0 PARA B MAYOR
if(anoa>anob):
    may=0
elif(anob>anoa):
    may=1
else:
    if(ma>mb):
        may=1
    elif(mb>ma):
        may=0
    else:
        if(da>db):
            may=1
        elif(db>da):
            may=0

cont=0
if(may==-1):
    print("Son iguales")
elif(may==1):
    while(anob>anoa):
        da,ma,anoa=diasiguiente(da,ma,anoa)
        cont+=1

elif(may==0):
    while(anoa>anob):
        db,mb,anob=diasiguiente(db,mb,anob)
        cont+=1

if(ma>mb):
    while(ma>mb):
        db,mb,anob=diasiguiente(db,mb,anob)
        cont+=1
else:
    while(mb>ma):
        da,ma,anoa=diasiguiente(da,ma,anoa)
        cont+=1
if(da>db):
    while(da>db):
        db,mb,anob=diasiguiente(db,mb,anob)
        cont+=1
else:
    while(db>da):
        da,ma,anoa=diasiguiente(da,ma,anoa)
        cont+=1
if(may!=-1):
    print("hay {} dias de diferencia entre ambas fechas".format(cont))
