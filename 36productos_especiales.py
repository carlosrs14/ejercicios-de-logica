#Escriba sendos programas que pidan al usuario la entrada correspondiente y calculen las siguientes operaciones:
#El factorial n! de un número entero n≥0, definido como:
#La potencia factorial creciente nm¯, definida como:
#(combinatoria)El coeficiente binomial (nk), definido como:
#El número de Stirling del segundo tipo S(n,k), que se puede calcular como:

#1
def factorial(n):
    if(n==0):
        return 1
    
    elif(n<0):
        return("No se puede")
    else:
        factor=1
        for i in range(1,n+1):
            factor= factor*i
        return factor
print(factorial(int(input("1) Ingresa tu n para calcular el factorial: "))))



#2
print("************************\nahora calcularemos la potencia factorial creciente")
x=int(input("Ingresa tu base o x: "))
n=int(input("Ingresa tu exponente o n: "))
acumulado=1
for i in range(0,n):
    acumulado *= (x+i)
    i+=1
print(f"Tu resultado es {acumulado}")



#3
print("************************\nahora calcularemos una combinatoria")
n= int(input("Ingresa tu n: "))
r = int(input("Ingresa tu r: "))
coeficienteb= factorial(n)//+(factorial(n-r)*factorial(r))
print(coeficienteb)
n= int(input("Número #4 Ingresa el número al que se le calculará el facotrial: "))
