import os 
os.system("cls")

numero=int(input("numero : "))

c4=numero%10
c3=int((numero%100)/10)
c2=int((numero%1000)/100)
c1=int(numero-(numero % 1000))/1000

print(str(c4)+str(c3)+str(c2)+str(c1))

