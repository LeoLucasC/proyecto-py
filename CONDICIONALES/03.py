import os
os.system ("cls")

angulo=int(input("EL ANGULO ES : "))

if angulo<90: print(angulo," ES ANGULO AGUDO")
elif angulo==90 : print(angulo," ES ANGULO RECTO")
elif angulo<180:print(angulo,"ES ANGULO OBTUSO")
elif angulo==180:print(angulo,"ES ANGULO LLANO")
elif angulo < 360 : print(angulo,"ES ANGULO CONCAVO")
elif  angulo==360 : print("ANGULO COMPLETO")
else : angulo>="error"
print()








