#El número de Euler, e ≈ 2,71828, puede ser representado como la siguiente suma infinita:
#Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia entre dos sumandos consecutivos sea menor que 0,0001.

def factorial(n):
    if(n==0):
        return 1
    
    elif(n<0):
        return("No se puede")
    else:
        factor=1
        for i in range(1,n+1):
            
            factor= factor*i

            pass
        return factor
        
e=0
i=0
numult=0
numpel=0
condicion=True
while(condicion):
    e= e+  1/factorial(i)
    print(e)
    i+=1
    condicion=1/factorial(i)-1/factorial(i+1)>0.0001