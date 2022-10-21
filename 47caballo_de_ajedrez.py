#dada la posición de un caballo en el tablero indque cuales pueden ser sus próximos movimientos
#fila=1-8, columna =a-h
posiciones=[1,2,3,4,5,6,7,8]
x= int(input("Ingrese la columna: "))
y= int(input("Ingrese la fila: "))
posibles=[]

if(x not in posiciones or y not in posiciones):
    print("La posición es invalida")   
else:
    for i in range(8):
        if(i%2==0):
            pass
        else:
            pass

        
        if((0<x and x<9) or (0<y and y<9)):
            pass