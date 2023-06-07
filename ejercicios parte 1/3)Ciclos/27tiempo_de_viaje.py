#Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él tiene la duración en minutos de cada uno de los tramos del viaje.
#Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total de viaje en formato horas:minutos.
#El programa deja de pedir tiempos de viaje cuando se ingresa un 0.
suma=0
while(True):
    n= int(input("Duración del tramo: "))
    suma+=n
    if (n ==0):
        break
horas=suma//60
minutos=suma%60
if(len(str(minutos))==1):
    print(f"El tiempo total de viaje fue: {horas}:0{minutos} horas")
else:
    print(f"El tiempo total de viaje fue: {horas}:{minutos} horas")
