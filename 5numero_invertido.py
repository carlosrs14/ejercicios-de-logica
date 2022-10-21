#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
numero= input("Ingrese un número de 3 cifras: ")
inverso=numero[2]+numero[1]+numero[0]
print(f"El numero invserso es: {inverso}")