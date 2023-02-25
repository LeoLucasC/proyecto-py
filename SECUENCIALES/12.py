import os
os.system ("cls")

tiempoensegundos=int(input("tiempo en segundos: "))

minuto=float(tiempoensegundos/60)
horas=float(minuto/60)
dias=(horas/24)

print(f"En minuto es: = {format(minuto, '.2f')}")
print(f"En Horas es: = {format(horas, '.5f')}")
print(f"En dias es: = {format(dias, '.2f')}")


