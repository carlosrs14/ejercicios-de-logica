#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:
potencia= int(input("Ingrese un número: "))

for i in range(0, potencia+1):
    print(2**i, end=" ")
