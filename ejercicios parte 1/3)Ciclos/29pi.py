#Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:
n= int(input("Ingresa el numero de sumas: "))
suma=0
contador=1
for i in range(1,n+1):
    if(i%2!=0):
        suma= suma+1/contador
    else:
        suma= suma-1/contador   
    contador+=2

print(4*suma)