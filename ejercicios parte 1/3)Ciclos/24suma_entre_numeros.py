#Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos. Por ejemplo, si los números son 1 y 7, debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.

ninicial = int(input("Ingresa desde que número la quieres calcular "))+1
nfinal = int(input("Ingresa hasta cual número quieres calcular "))-1

if (ninicial<=nfinal):
    s = (nfinal*(nfinal+1)//2) - ((ninicial-1)*(ninicial)//2)
    print(f"tu resultado con la formula de gauss es: {s}")
else:
    print("tu número inicial fue mayor que número final")