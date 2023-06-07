#Entre todos los enteros mayores a 1 hay solamente cuatro que pueden ser representados por la suma de los cubos de sus dígitos.

cumplen=[]

for i in range(150, 411):

    n1=int(str(i)[0])         
    n2=int(str(i)[1])
    n3=int(str(i)[2])
    if(n1**3+n2**3+n3**3==i):
        cumplen.append(i)
print(cumplen)

