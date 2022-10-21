#Escriba un programa que indique si el número ingresado es o no palíndromo:

palabra= input("Ingrese una palabra: ")
invertida=""
for i in range(len(palabra),0,-1):
    invertida+=palabra[i-1]
if palabra == invertida:
    print(f"{palabra} es palíndroma")
else:
    print(f"{palabra} no es palidroma")

frase = input("Ahora probemos con una frase: ")
frasecopy = frase
frase=frase.replace(" ","")
invertida=""
for i in range(len(frase),0,-1):
    invertida+=frase[i-1]
if frase == invertida:
    print(f"{frasecopy} es palíndroma")
else:
    print(f"{frasecopy} no es palidroma")