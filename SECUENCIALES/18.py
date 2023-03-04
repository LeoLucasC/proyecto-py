import os 
os.system("cls")
articulos=int(input("NUMERO DE ARTICULOS: "))
venta=int(input("PRECIO POR  ARTICULO: S/"))
print("*"*20)
print("EL DESCUENTO DE 15% + 15%")

quiere=(articulos*venta)

importe1=(quiere*15)/100
importcompra=(quiere-importe1)

importe2=(importcompra*15)/100
print("EL TOTAL CON EL DESCUENTO ES: ",importe2)






