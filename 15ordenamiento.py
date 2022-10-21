#Escriba un programa que reciba como entrada dos números, y los muestre ordenados de menor a mayor:
n = int(input("cual es la cantidad de números que va a ingresar? "))
lista=[]
for i in range(0,n):
    s=i
    numero= int(input(f"Ingrese el {s+1}-ésimo número: "))
    lista.append(numero)

lista=sorted(lista)
for i in lista:
    print(i, end=" ")