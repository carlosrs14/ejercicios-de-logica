#Escriba un programa que pida al usuario que ingrese varios valores enteros, que pueden ser positivos o negativos. Cuando se ingrese un cero, el programa debe terminar y mostrar un gráfico de cuántos valores positivos y negativos fueron ingresados:
numero=1
positivos=0
negativos=0
print("Ingrese varios valores y termine con \"0\":")
while(numero!=0):
    numero=int(input())
    if(numero>0):
        positivos+=1
    elif(numero<0):
        negativos+=1

print("Positivos: ", "*"*positivos)
print("Negativos: ", "*"*negativos)



