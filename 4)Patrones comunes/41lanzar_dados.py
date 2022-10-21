#Escriba un programa que muestre todas las combinaciones posibles al momento de lanzar dos dados de 6 caras:

for i in range(1,7):
    for j in range(1,7):
        print(f"{i} {j}")
    print("\n")