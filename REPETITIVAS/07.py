import os 
os.system

numero=int(input("NUMERO: "))
factorial=1

if numero!=0:
    for i in range(1,numero+1):
        factorial=factorial*i

print("FACTORIAL: ",factorial)
 




