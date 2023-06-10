# El índice de masa corporal es el cuociente entre el peso del individuo en kilos y el cuadrado de su estatura en metros.
# Escriba un programa que reciba como entrada la estatura, el peso y la edad de una persona, y le entregue su condición de riesgo.

edad=int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso: "))
estatura =float(input("Ingresa tu estatura: "))
imc = peso/estatura**2
if (edad<45):
    if(imc<22.0):
        print("Bajo")
    else:
        print("Medio")

else:
    if(imc<22.0):
        print("Medio")
    else:
        print("Alto")
print(f"Y tu imc es {imc}")
