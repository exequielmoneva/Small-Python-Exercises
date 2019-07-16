"""Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. Por ejemplo, para (12,10,17) devuelve "12 de Octubre de
2017". Escribir también un programa para verificar su comportamiento."""
try:
    def di(fecha,dict):
        res=""
        res=fecha[0]," de ", dict[fecha[1]]," de ",fecha[2]
        return res
        
        
        
    d=int(input("Ingrese dia: "))
    m=int(input("Ingrese mes: "))
    while(m<0 or m>12):
        m=int(input("Ingrese mes: "))
    a=int(input("Ingrese año: "))
    fecha=d,m,a
    dict={
        1:"Enero",
        2:"Febrero",
        3:"Marzo",
        4:"Abril",
        5:"Mayo",
        6:"Junio",
        7:"Julio",
        8:"Agosto",
        9:"Septiembre",
        10:"Octubre",
        11:"Noviembre",
        12:"Diciembre"
        }
    func= di(fecha,dict)
    for i in range (len(func)):
        print(func[i], end="")
except ValueError:
    print("El valor ingresado no es valido")