#Escriba un programa que indique si el número ingresado es o no palíndromo:

numero= input("Ingrese un numero: ")
invertido=""
for i in range(len(numero),0,-1):
    invertido+=numero[i-1]
if numero == invertido:
    print(f"{numero} es un número palíndromo")
else:
    print(f"{numero} no es palidromo")