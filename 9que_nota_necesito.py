#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.
nota1 = int(input("Ingrese la nota primer certamen: "))
nota2 = int(input("Ingrese la nota segundo certamen: "))
notaLab= int(input("Ingrese la nota del laboratorio: "))

faltante = 3*(60-notaLab*0.3)/0.7 - nota1 - nota2

print(f"Necesita una nota de {faltante} en el certamen 3")