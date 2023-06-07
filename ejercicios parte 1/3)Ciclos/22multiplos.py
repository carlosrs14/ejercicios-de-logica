#Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:
n= int(input("Ingrese un número: "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")