import os
os.system("cls")

kilometros=int(input("kilometros: "))
pies=int(input("pies: "))
millas=int(input("millas: "))


metro=kilometros*1000
pies = metro/ 3280.84
millas=metro/1609.34




print(f"el primer tramo en metro es: {format(metro,' .2f')} ")
print(f"el segundo  tramo en pies     es:{format(metro,' .2f')}")
print(f"el tercer tramo en millas     es:{format(millas,' .2f')} ")
