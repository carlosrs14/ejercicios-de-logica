sumas=[]
rango=200
#while(len(sumas)<2):

for i in range(-rango, rango):
    for j in range(-rango, rango):
        for k in range(-rango, rango):
            suma=i**3 + j**3 + k**3
            if(suma==100):
                sumas.append([i,j,k])
            print(sumas, i, j, k)

print(sumas)