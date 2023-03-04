import os 
os.system("cls")

print("SUELDO BASICO DEL VENDEDOR ES S/ 5OO.00")

montovendido=int(input("MONTO VENDIDO : S/ "))

sueldobasico=500

comision=(montovendido*9)/100
print("LA COMISION  DEL 9% ES : S/",comision)
sueldobruto=(sueldobasico+comision)
descuento11=(sueldobruto*11)/100
descuento12=sueldobruto-descuento11

print("EL SUELDO BRUTO ES : S/ ",sueldobruto)
print("EL DESCUENTO DEL 11% ES : S/",descuento11)
print("TOTAL CON EL DESCUENTO ES :S/ ",descuento12)
print("EL SUELDO NETO ES : S/",descuento12)






