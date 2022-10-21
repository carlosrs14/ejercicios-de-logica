#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
if (dividendo%divisor!=0):
    print("La división no es exacta.")
    print(f"Cociente: {dividendo//divisor}")
    print(f"Residuo: {dividendo%divisor}")
else:
    print("La división es exacta.")
    print(f"Cociente: {dividendo//divisor}")
    print(f"Residuo: {dividendo%divisor}")

