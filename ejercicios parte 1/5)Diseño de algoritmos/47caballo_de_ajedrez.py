#dada la posición de un caballo en el tablero indque cuales pueden ser sus próximos movimientos
#fila=1-8, columna =a-h
posiciones=[1,2,3,4,5,6,7,8]
x= int(input("Ingrese la columna: "))
y= int(input("Ingrese la fila: "))
posibles=[]

if(x not in posiciones or y not in posiciones):
    print("La posición es invalida")   
else:
    #x-2 y+1 // x-2 y-1
    if(x-2 in posiciones):
        if(y+1 in posiciones):
            posibles.append([x-2, y+1])
        if(y-1 in posiciones):
            posibles.append([[x-2, y-1]])

    #x-1 y+2 // x-1 y-2
    if(x-1 in posiciones):
        if(y+2 in posiciones):
            posibles.append([x-1, y+2])
        if(y-2 in posiciones):
            posibles.append([[x-1, y-2]])

    #x+2 y+1 // #x+2 y-1
    if(x+2 in posiciones):
        if(y in posiciones):
            posibles.append([x+2, y+1])
        if(y-1 in posiciones):
            posibles.append([[x+2, y-1]])

    #x+1 y+2 // #x+1 y-2
    if(x+1 in posiciones):
        if(y+2 in posiciones):
            posibles.append([x+1, y+2])
        if(y-2 in posiciones):
            posibles.append([[x+1, y-2]])
if(len(posibles)>0):
    print(f"Los movimientos posibles de este caballo son {posibles}")