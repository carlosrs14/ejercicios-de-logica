#Escriba un programa que entregue la edad del usuario a partir de su fecha de nacimiento:
from time import localtime

print("ingrese su fecha de nacimiento para calcular tu edad")
diaNa=int(input("Día: "))
mesNa=int(input("Mes: "))
anioNa=int(input("Año: "))

diaAc = localtime().tm_mday
mesAc = localtime().tm_mon
anioAc = localtime().tm_year

if (diaNa<=diaAc):
    if (mesNa<=mesAc):
        edad = anioAc-anioNa
    else:
        edad = anioAc-anioNa-1
else:
    if (mesNa<=mesAc):
        edad = anioAc-anioNa-1
    else:
        edad = anioAc-anioNa-1

if (edad>=0):
    print(f"Tu edad es: {edad}")
else:
    print("Aún no naces")


