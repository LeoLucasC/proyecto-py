import os
import math
os.system ("cls")

radio=int(input("Radio: "))
altura=int(input("Altura: "))

areabase=math.pi*(radio**2)
arealateral=2*math.pi*radio*altura
areatotal=2*areabase*arealateral

print(f"AREA DE LA BASE ={format(areabase, '.2f')}")
print(f"AREA LATERAL = {format(arealateral, '.2f')}")
print(f"AREA TOTAL= {format(areatotal, '.2f')}")

