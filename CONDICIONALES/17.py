import os 
os.system("cls")

docenalapicero=int(input("DOCENA DE LA PICEROS: "))

if docenalapicero>=6: 
    print("EL DESCUENTO POR ESA CANTIDAD ES 15%")
    descuento=(docenalapicero*15)/100
    print(f"EL DESCUENTO DEL 15%       : {format(descuento, '.2f')} ")
    total=docenalapicero-descuento
    print("EL TOTAL CON EL DESCUENTO ES: ",total)
    if docenalapicero>30 and docenalapicero%3==0: 
        divisor=(docenalapicero/3)*2
        print("EL OBSEQUIO ES          : ",divisor)
    total1=total+divisor
    print("El total es",total1)

elif docenalapicero<=6: 
    print("EL DESCUENTO POR ESA CANTIDAD ES 10%")
    descuento=(docenalapicero*10)/100
    print(f"EL DESCUENTO DEL 10 ={format(descuento, '.2f')} ")
    total=docenalapicero-descuento
    print("EL TOTAL CON EL DESCUENTO ES: ",total)
    if docenalapicero<30 and docenalapicero%3!=0: 
        sinobsequio="NO TIENE OBSEQUIO"
        print(sinobsequio)
    print("EL TOTAL ES :",total)










