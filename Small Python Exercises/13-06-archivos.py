"""Escribir un programa que permita grabar un archivo los datos de lluvia caída durante un año.
Cada línea del archivo se grabará con el siguiente formato: <dia>;<mes>;<lluvia caída en mm> por ejemplo 25;5;319
Los datos se generarán mediante números al azar, asegurándose que las fechas sean válidas.
La cantidad de registros también será un número al azar entre 50 y 200.
Por último se solicita leer el archivo generado e
imprimir un informe en formato matricial donde cada columna represente a un mes
y cada fila corresponda a los días del mes. Imprimir además el total de lluvia caída en todo el año."""
import random
try:
    arch=open(r"D:\Users\EMONEVA\Desktop\clima.txt","wt")#SE DEBE MODIFICAR LA DIRECCION PARA TEST
    cant=random.randint(50,200)
    n=0
    while (n<=cant):
        dia=random.randint(1,31)
        mes=random.randint(1,12)
        mm=random.randint(0,1000)
        arch.write("{};{};{}\n".format(dia,mes,mm))
        n+=1
        
except NameError:
    print("???")

finally:
    try:
        arch.close()
    except NameError:
        pass