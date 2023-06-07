#dados los juegos de dos jugadores de tennis determina quien ganó el set, si es invalido o si aún no termina
jugador1 = int(input("Ingresa los sets ganados por el jugador #1: "))
jugador2 = int(input("Ingresa los sets ganados por el jugador #2: "))

if(jugador1==6):
    if(jugador1-jugador2<2):
        print("Aún no termina")
        exit(0)
    else:
        print("Ganó el jugador 1")
        exit(0)
if(jugador1==7):
    if(jugador1-jugador2<2):
        print("Aún no termina")
        
    elif((jugador1-jugador2>3)):
        print("Reslutado invalido")
        
    else:
        print("Ganó el jugador 1")
    exit(0)
if(jugador2==6):
    if(jugador2-jugador1<2):
        print("Aún no termina")
    else:
        print("Ganó el jugador 2")
    exit(0)
if(jugador2==7):
    if(jugador2-jugador1<2):
        print("Aún no termina")
    elif((jugador2-jugador1>3)):
        print("Resultado invalido")
    else:
        print("Ganó el jugador 2")
        exit(0)
elif(jugador1<6 and jugador2<6 or jugador1==jugador1):
    print("Aún no termina")
elif(jugador1>=8 or jugador2>=8):
    print("Resultado invalido")