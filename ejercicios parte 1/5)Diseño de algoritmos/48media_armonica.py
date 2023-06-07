#Desarrolle un programa que calcule la media armónica de una secuencia de números.

n=int(input("Cuantos números ingresaras: "))
denominador=0
for i in range(n):
    numero=int(input(f"n{i+1} = "))
    denominador+=(1/numero)
print(f"La media armónica es: {n/denominador}")

