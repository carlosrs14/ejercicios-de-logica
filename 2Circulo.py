#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:
import math

radio = int(input("Ingrese el radio: "))
perimetro = 2 * math.pi * radio
area = math.pi * radio**2

print(f"Perimetro es: {perimetro}")
print(f"Área es: {area}")