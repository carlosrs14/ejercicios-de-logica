#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

actual = int(input("Ingrese la hora actual: "))
incremento= int(input("Ingrese la hora cantidad de horas a adelantar: "))
hFutura = actual+incremento
if(hFutura>=12):
    hFutura=hFutura%12
    
print(f"En {incremento} horas, el reloj marcará las {hFutura}")