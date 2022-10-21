#Escriba un programa que muestre los números naturales menores o iguales que un número n determinado, que no sean múltiplos ni de 3 ni de 7.

n=int(input("Ingrese número: "))
for i in range(1, n+1):
    if(i%3!=0 and i%7!=0):
        print(i)


