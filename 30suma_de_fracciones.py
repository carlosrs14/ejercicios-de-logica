#Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir:
#1/2,1/4,1/8,1/16,1/32,1/64,…
#El programa debe terminar cuando la fracción decimal sea menor o igual a 0.000001.

fracccion=1
suma=0
i=1
print("potencia fraccion suma")
while(fracccion>=0.000001):
    fracccion=0
    fracccion=1/2**i
    suma+=fracccion
    print(f"{i}***{fracccion}***{suma}")
    i+=1




