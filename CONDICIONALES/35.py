import os
os.system ("cls")

codigo=int(input("COLOCA EL CODIGO: "))

divisible2=codigo%2==0
divisible3=codigo%3==0
divisible5=codigo%5==0

if         divisible2 and divisible3 and divisible5 : tipo = "Administrativo"
elif not   divisible2 and divisible3 and divisible5 : tipo = "Directivo"
elif       divisible2 and not divisible3 and not divisible5 : tipo = "vendedor"
elif not   divisible2 and not  divisible3 and not divisible5 == 0: tipo = "seguridad"
else : tipo="error"


print(f"tipo={tipo}")
print()











