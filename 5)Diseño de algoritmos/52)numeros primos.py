#1)Escriba un programa que reciba como entrada un número natural, e indique si es primo o compuesto:
#2)Escriba un programa que muestre los n primeros números primos, donde n es ingresado por el usuario:
#3)Escriba un programa que muestre los números primos menores que m, donde m es ingresado por el usuario:
#4)Escriba un programa que cuente cuántos son los números primos menores que m, donde m es ingresado por el usuario:
#5)Escriba un programa que muestre los factores primos de un número entero ingresado por el usuario:
#6)Escriba un programa que reciba un número par como entrada y muestre todas las maneras en que puede ser escrito como una suma de dos primos:
#7)Escriba programas que respondan las siguientes preguntas:
#-¿Cuántos primos menores que diez mil terminan en 7?
#-¿Cuál es la suma de los cuadrados de los números primos entre 1 y 1000? (Respuesta: 49.345.379).
#-¿Cuál es el producto de todos los números primos menores que 100 que tienen algún dígito 7? (Respuesta: 7 × 17 × 37 × 47 × 67 × 71 × 73 × 79 × 97 = 550.682.633.299.463).

from numpy import append


def esPrimo(numero):
    i=3
    if(numero>=0 and numero<=3):
        return True
    if(numero%2==0):
        return False
    mitad=numero//2+1
    while(i<numero**(1/2)+1):
        if(numero%i==0):
            return False
        i+=2
    return True

#solución 1
numero=int(input("Ingrese un número: "))
if(esPrimo(numero)):
    print(f"{numero} es primo")
else:
    print(f"{numero} es compuesto")
print("\n")


#solución 2
i=2
primos=[]
print("Los primeros n primos")
n=int(input("Ingresa n: "))
while(len(primos)<n):
    if(esPrimo(i)):
        primos.append(i) 
    i+=1
print(primos)
print("\n")


#solución 3
primos=[]
print("primos menores que n: ")
n=int(input("Ingresa n: "))
for i in range(2,n):
    if(esPrimo(i)):
        primos.append(i)
print(primos)
print("\n")


#solución 4
nprimos=1    
print("primos menores que n: ")
n=int(input("Ingresa n: "))
for i in range(3,n, 2):
    if(esPrimo(i)):
        nprimos+=1
print(f"Hay {nprimos} primos menores que {n}")
print("\n")


#solución 5
print("factorización de n")
n=int(input("Ingresa n: "))
factores = []
i=2
while(n!=1):
    while(n%i==0):
        n=n%i
        factores.append(i)    
    i+=1
for i in range(factores):
    print(factores[i])
