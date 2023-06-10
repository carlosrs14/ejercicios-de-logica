#Escriba un programa que determine si un caracter ingresado es letra, número, o ninguno de los dos. En caso que sea letra, determine si es mayúscula o minúscula.

numeros= ["0","1","2","3","4","5","6","7","8","9"]
mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

minusculas =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
entrada = input("Ingresa un caracter: ")



if entrada in minusculas:
    print("Tu entrada es una minuscula")
elif entrada in mayusculas:
    print("Tu entrada es una mayuscula")
elif entrada in numeros:
    print("Tu entrada es un número")
else:
    print("Tu entrada no es número ni letra")