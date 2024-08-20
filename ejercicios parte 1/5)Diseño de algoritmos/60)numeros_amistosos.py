#Muchos pares de números amigables son conocidos; sin embargo, sólo uno de los pares (220, 284) tiene valores menores que 1000. El siguiente par está en el rango [1000, 1500].
#Desarrolle un programa que permita encontrar dicho par.
par = []
divisores1 = []
divisores2 = []
sumadivisores1 = 0
sumadivisores2 = 0
for i in range(1000, 1501):
    for j in range(1, i):
        if(i % j == 0):
            divisores1.append(j)
    for k in divisores1:
        sumadivisores1 += k
    numero2 = sumadivisores1
    for l in range(1, numero2):
        if(numero2 % l == 0):
            divisores2.append(l)
    
    for m in divisores2:
        sumadivisores2 += m
    if(sumadivisores1 == numero2 and sumadivisores2 == i):
        par.append([i, numero2])

    divisores1 = []
    divisores2 = []
    sumadivisores1 = 0
    sumadivisores2 = 0
print(par)