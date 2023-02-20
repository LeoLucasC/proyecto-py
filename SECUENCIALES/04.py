import os 
os.system ("cls")

#pies a metros = 0.3048
#pulgadas a metros = 0.0254

pies=int(input("pies: "))
pulgadas=int(input("pulgadas: "))

metro=pies*3.28
pulgadas=metro/39.37

sumaestatura=metro+pulgadas

print(f"Estatura = {format(sumaestatura,' .2f')} ")


