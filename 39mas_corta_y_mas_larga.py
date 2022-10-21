#primero, el usuario ingresa un número entero n, que indica cuántas palabras ingresará a continuación;
#después el usuario ingresa n palabras.
#La salida del programa debe mostrar la palabra más larga y la más corta que fueron ingresadas por el usuario.
n=int(input("Cantidad de palabras: "))

for i in range(1,n+1):
    palabra=input(f"Palabra {i}: ")
    if (i==1):
        larga=palabra
        corta=palabra
    else:
        if(len(palabra)<len(corta)):
            corta=palabra
        if(len(palabra)>len(larga)):
            larga=palabra    
print(f"La palabra más larga es {larga} y la más corta es {corta}")

