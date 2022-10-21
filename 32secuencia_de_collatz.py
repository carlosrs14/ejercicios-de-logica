#la sucesión termina al llegar a uno.
#si el número es par, se lo divide por dos;
#si es impar, se le multiplica tres y se le suma uno;
#la sucesión termina al llegar a uno.


n= int(input("Ingresa el número al que se le va a calcular la secuencia: "))
ncopy1=n
ncopy2=n
contador=1


print(f"La secuecia del numero que ingresaste es:\n{n}", end=" ")
while(n!=1):
    if(n%2==0):
        n=n//2
    else:
        n=n*3+1
    contador+=1
    print(n, end=" ")

print("\nRepresentado graficamente las primeros n números sería:\n")

for i in range(1,ncopy2+1):
    contador=1
    numero=i
    while(i!=1):
        if(i%2==0):
            i=i//2
        else:
            i=i*3+1
        contador+=1
        
        
    print(numero, "*"*contador, "\n")
    
