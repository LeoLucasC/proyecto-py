import os 
os.system ("cls")

horas=int(input("tiempo en HORAS: "))
minutos=int(input("tiempo en MINUTOS: "))
segundos=int(input("tiempo en SEGUNDOS: "))

suma=minutos+45

if suma>=60:
    suma=suma-60 
    horas=horas+1
if segundos>=60:
    segundos=segundos-60
    suma=suma+1
if horas>24 :
    horas=(horas-25)+1

print("TIEMPO TRAS 45 MIN")
print(f"{horas}:{minutos}:{segundos}")

    



