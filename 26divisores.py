#Escriba un programa que entregue todos los divisores del número entero ingresado:
n = int(input("Ingrese un número: "))

for i in range(1,n//2+1):
    if(n%i==0):
        print(i, end=" ")
print(n)

