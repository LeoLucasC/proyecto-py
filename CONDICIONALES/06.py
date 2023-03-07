import os
os.system("cls")

edad=int(input("COLOQUE SU 1eraEDAD: "))
edad1=int(input("COLOQUE SU 2eraEDAD: "))
edad2=int(input("COLOQUE SU 3eraEDAD: "))


# primer ingreso

if edad<18 : tipo="Usted es menor de edad"
elif edad>18 and edad<60 : tipo="Usted es mayor de edad"
elif edad>=60 : tipo="Usted es un adulto mayor"
else : edad="ERROR"
print(tipo)

#segundo  ingreso

if edad1<18 : tipo="Usted es menor de edad"
elif edad1>18 and edad1<60 : tipo="Usted es mayor de edad"
elif edad1>=60 : tipo="Usted es un adulto mayor"
else : edad="ERROR"
print(tipo)

#Tercer ingreso

if edad2<18 : tipo="Usted es menor de edad"
elif edad2>18 and edad2<60 : tipo="Usted es mayor de edad"
elif edad2>=60 : tipo="Usted es un adulto mayor"
else : edad="ERROR"
print(tipo)















