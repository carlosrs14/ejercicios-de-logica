#Un jugador debe lanzar dos dados numerados de 1 a 6, y su puntaje es la suma de los valores obtenidos.
#Un puntaje dado puede ser obtenido con varias combinaciones posibles. Por ejemplo, el puntaje 4 se logra con las siguientes tres combinaciones: 1+3, 2+2 y 3+1.
#Escriba un programa que pregunte al usuario un puntaje, y muestre como resultado la cantidad de combinaciones de dados con las que se puede obtener ese puntaje.

puntaje=int(input("Ingrese el puntaje: "))
posibles=0
for i in range(1,7):
    for j in range(1,7):
        if((i+j)==puntaje):
            posibles+=1
print(f"Hay {posibles} combinaciones para obtener {puntaje}")