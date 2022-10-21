#Escriba un programa que reciba como entrada los tres lados de un triángulo, e indique:
#si acaso el triángulo es inválido; y
#si no lo es, qué tipo de triángulo es.
lado1=float(input("Ingresa el tamaño del lado #1: "))
lado2=float(input("Ingresa el tamaño del lado #2: "))
lado3=float(input("Ingresa el tamaño del lado #3: "))

if(lado1==lado2 and lado1==lado3):
    print("El triangulo es equilatero")
elif(lado1==lado2 or lado1==lado3 or lado2==lado3):
    print("El triangulo es isoceles")
elif(lado1>lado2+lado3 or lado2>lado1+lado3 or lado3>lado1+lado2):
    print("Triangulo invalido")
else:
    print("Es triangulo es escaleno")   
