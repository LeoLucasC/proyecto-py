import os 
os.system ("cls")

gigabytes=int(input("GIGABYTES: "))

megabytes=gigabytes*1024
kilobytes=megabytes*1024
bytes=kilobytes*1024

print(f"MEGABYTES = {format(megabytes,' .1f')} ")
print(f"KILOBYTES = {format(kilobytes,' .1f')} ")
print(f"BYTES = {format(bytes,' .2f')} ")


