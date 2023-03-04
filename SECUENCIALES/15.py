import os 
os.system("cls")

juan=int(input("APORTE DE JUAN EN DOLARES  : "))
rosa=int(input("APORTE DE ROSA EN DOLARES  : "))
daniel=int(input("APORTE DE DANIEL EN SOLES S/: "))

daniel=daniel*3

capitaltotal=daniel+rosa+juan
print("EL CAPITAL EN DOLARES ES : ",capitaltotal)

porcentajejuan=(juan*100)/capitaltotal
print(f"EL PORCENTAJE DE JUAN EN EL MONTO ES DE: %{format(porcentajejuan, '.2f')}")

porcentajerosa=(rosa*100)/capitaltotal
print(f"EL PORCENTAJE DE ROSA EN EL MONTO ES DE: %{format(porcentajerosa, '.2f')}")


porcentajedaniel=(daniel*100)/capitaltotal
print(f"EL PORCENTAJE DE DANIEL EN EL MONTO ES DE: %{format(porcentajedaniel, '.2f')}")






