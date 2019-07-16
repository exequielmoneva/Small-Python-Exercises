"""Escribir un programa que lea un archivo de texto conteniendo un conjunto de
apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los nombres de aquellas personas cuyo apellido terminan con la
cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en el archivo
ESPAÑA.TXT los terminados en "EZ". Descartar el resto. Ejemplo:
Arslanian, Gustavo –> ARMENIA.TXT
Rossini, Giuseppe –> ITALIA.TXT
Pérez, Juan –> ESPAÑA.TXT
Smith, John –> descartar
El archivo de entrada puede ser creado mediante el Block de Notas o el IDLE. No
escribir un programa para generarlo."""
try:
    arch=open(r"T:\nn.txt","rt")
    ita=open(r"T:\ITALIA.txt","wt")
    arm=open(r"T:\ARMENIA.txt","wt")
    esp=open(r"T:\ESPAÑA.txt","wt")
    linea=arch.readline()
    while(linea):
        apellido,nombre=linea.split(",")
        nombre=nombre.rstrip("\n")
        apellido=list(apellido)
        aux=apellido[len(apellido)-3:]
        au=apellido[len(apellido)-2:]
        aux="".join(aux)
        au="".join(au)
        print(aux)
        print(au)
        if(aux.lower()=="ini"):
           ita.writelines(linea)
        elif(aux.lower()=="ian"):
            arm.writelines(linea)
        elif(au.lower()=="ez"):
            esp.writelines(linea)
        linea=arch.readline()
except SyntaxError:
    print("Ups")
finally:
    try:
        arch.close()
        ita.close()
        arm.close()
        esp.close()
    except NameError:
        pass