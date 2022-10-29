#Escriba un programa que reciba como entrada un número entero n, y entregue como salida el n-ésimo número de Fibonacci:
print("Se calculará el n-ésimo de la secuencia fibonacci")
n=int(input(("Ingresa el n: ")))
fibonacci=[0,1]
n1=0
n2=1
while(len(fibonacci)<=n):
    n3=n1+n2
    n1=n2
    n2=n3
    fibonacci.append(n3)
print(f"F{n} = {fibonacci[n]}")

#Escriba un programa que reciba como entrada un número entero e indique si es o no un número de Fibonacci:
print("Este verá si el número ingresado pertenece a la secuencia  fibonacci")
n=int(input(("Ingresa el n: ")))
fibonacci=[0,1]
n1=0
n2=1
n3=0
while(n3<=n):
    n3=n1+n2
    n1=n2
    n2=n3
    fibonacci.append(n3)
if(n in fibonacci):
    print(f"{n} pertenece")
else:
    print("No pertenece")

#Escriba un programa que muestre los m primeros números de Fibonacci, donde m es un número ingresado por el usuario:
print("mostrará los primero n fiboacci")
n=int(input(("Ingresa el n: ")))
fibonacci=[0,1]
n1=0
n2=1
while(len(fibonacci)<n):
    n3=n1+n2
    n1=n2
    n2=n3
    fibonacci.append(n3)

for i in fibonacci:
    print(i, end=" ")


