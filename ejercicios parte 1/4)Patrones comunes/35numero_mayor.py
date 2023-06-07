n=int(input("Ingrese cuantos números comparará: "))
for i in range(0,n):
    numero=int(input("Ingrese un número: "))
    if(i==0):
        mayor=numero
    else:
        if(numero>mayor):
            mayor=numero
print(f"El mayor es {mayor}")