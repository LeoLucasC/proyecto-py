import os 
os.system("cls")

importe=int(input("COLOQUE EL IMPORTE: "))



if importe>700 :
    print("EL DESCUENTO ES DE 16%")
    unidades=importe/20
    descuento=(importe*16)/100
    total=importe-descuento
    print("CON EL DESCUENTO ES : ",total)
    if unidades<=50 : print("SE LE DA CARAMELOS : 5 ")
    elif unidades>51 and unidades<=100 : print("SE LE DA DE CARAMELOS : 10")
    elif unidades>100 : print("SE LE DA DE CARAMELOS : 15")

elif importe>501 and importe<=700 :
    print("EL DESCUENTO ES DE 14%")
    unidades=importe/20
    descuento=(importe*14)/100
    total=importe-descuento
    print("CON EL DESCUENTO ES : ",total)
    if unidades<=50 : print("SE LE DA CARAMELOS : 5 ")
    elif unidades>51 and unidades<=100 : print("SE LE DA DE CARAMELOS : 10")
    elif unidades>100 : print("SE LE DA DE CARAMELOS : 15")
elif importe<=500 :
    print("EL DESCUENTO ES DE 12%")
    unidades=importe/20
    descuento=(importe*12)/100
    total=importe-descuento
    print("CON EL DESCUENTO ES : ",total)
    if unidades<=50 : print("SE LE DA CARAMELOS : 5 ")
    elif unidades>51 and unidades<=100 : print("SE LE DA DE CARAMELOS : 10")
    elif unidades>100 : print("SE LE DA DE CARAMELOS : 15")   
   

















