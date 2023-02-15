varones=int(input("varones: "))
mujeres=int(input("mujeres: "))

total=varones+mujeres
pvarones=varones*100.0 /total
pmujeres=mujeres*100.0 /total

print(f"porcentaje de varones es={format(pvarones,' .2f')}%")
print(f"porcentaje de mujeres es={format(pmujeres,' .2f')}%")
print("")