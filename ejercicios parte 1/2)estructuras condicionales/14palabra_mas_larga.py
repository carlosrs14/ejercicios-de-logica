#Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más larga y por cuántas letras lo es.
palabra1 = input("Palabra 1: ")
palabra2 = input("Palabra 2: ")
if (len(palabra1)>len(palabra2)):
    print(f"La palabra {palabra1} tiene {len(palabra1)-len(palabra2)} letras más que {palabra2}.")
elif(len(palabra1)<len(palabra2)):
    print(f"La palabra {palabra2} tiene {len(palabra2)-len(palabra1)} letras más que {palabra1}.")
else:
    print(f"Las palabras {palabra2} y {palabra1} tienen la misma cantidad de letras.")
