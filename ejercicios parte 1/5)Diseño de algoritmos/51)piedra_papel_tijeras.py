#Escriba un programa que pregunte a cada jugador cuál es su jugada, muestre cuál es el marcador después de cada ronda, y termine cuando uno de ellos haya ganado tres rondas. Los jugadores deben indicar su jugada escribiendo
#El ganador del juego es el primero que gane tres rondas.

marcadorA=0
marcadorB=0
print("\nBienvenido al juego piedra, papel o tijeras")

while(marcadorA<3 and marcadorB<3):
    #input("Ingresa enter para continuar")
    print("\nTus opciones son:\nPierda:\t1\nPapel:\t2\nTijera:\t3")
    jugadaA = int(input("Jugador A ingresa tu jugada: "))
    jugadaB = int(input("Jugador B ingresa tu jugada: "))
    print("\n")
    if(jugadaA==1):
        if(jugadaB==1):
            print("Empate")
        
        elif(jugadaB==2):
            print("Jugador B gana")
            marcadorB+=1
        elif(jugadaB==3):
            print("Jugador A gana")
            marcadorA+=1
        else:
            print("Jugada invalida")
            pass
    elif(jugadaA==2):
        if(jugadaB==2):
            print("Empate")
        
        elif(jugadaB==3):
            print("Jugador B gana")
            marcadorB+=1
        elif(jugadaB==1):
            print("Jugador A gana")
            marcadorA+=1
        else:
            print("Jugada invalida")
            pass
    elif(jugadaA==3):

        if(jugadaB==3):
            print("Empate")
        
        elif(jugadaB==1):
            print("Jugador B gana")
            marcadorB+=1
        elif(jugadaB==2):
            print("Jugador A gana")
            marcadorA+=1
        else:
            print("Jugada invalida")
            pass
    else:
        print("Movimiento invalido")
        pass
    print(f"{marcadorA} - {marcadorB}\n")

if(marcadorA==3):
    print("Ganó el jugador A")
else:
    print("Ganó el jugaor B")