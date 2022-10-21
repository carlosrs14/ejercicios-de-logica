#Desarrolle un programa que permita determinar la cantidad total de puntos que contiene un juego de dominó de 28 piezas.
puntos=0
combinaciones=[]
for i in range(0,7):
    for j in range(0,7):
        if(i>j):
            lista=[i,j]
        else:
            lista=[j,i]
        if lista not in combinaciones:
            combinaciones.append(lista)
print(combinaciones)
cont=0
for i in combinaciones:
    for j in combinaciones[cont]:
        puntos+=j
    cont+=1

print("El total de puntos que tiene un dominó es: ", puntos)