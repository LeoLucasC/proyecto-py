import os 
os.system ("cls")

nota1=int(input("1ra nota: "))
nota2=int(input("1ra nota: "))
nota3=int(input("1ra nota: "))


if nota3>=10 and nota3<=18 :
    nota3=nota3+2

promedio=(nota1+nota2+nota3)/3

print(f"EL PROMEDIO ES:{format(promedio, '2f')}")





