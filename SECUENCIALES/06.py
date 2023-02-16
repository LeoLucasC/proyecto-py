import os
import math
os.system("cls")

radio=int(input("Radio: "))
altura=int(input("Altura: "))

areaCilindro = 2 * 3.14 * radio * (radio + altura)
volumencilindro = math.pi * math.pow(radio,2)* altura
print(f"Area={format(areaCilindro,'.2f')} u2 ")
print(f"Area={format(volumencilindro,'.2f')} u3 ")
print()
