#Desarrolle un programa que calcule el dígito verificador de un rol UTFSM.
#Para calcular el dígito verificador, se deben realizar los siguiente pasos:

#1)Obtener el rol sin guión ni dígito verificador.
numero=int(input("Ingrese el número: "))
invertido=""
#2)invertir el numero
for i in range(len(str(numero))-1,-1,-1):
    invertido=invertido+str(numero)[i]

#3)Multiplicar los dígitos por la secuencia 2, 3, 4, 5, 6, 7, si es que se acaban los números, se debe comenzar denuevo
factor=2
acumulador=0
for i in range(0, len(str(numero))):
    acumulador += factor*int(invertido[i])
    if(factor==7):
        factor=1
    factor+=1

#4)Al resultado obtenido, es decir, 52, debemos sacarle el módulo 11, es decir:
resultado=acumulador%11

#5)Con el resultado obtenido en el paso anterior, debemos restarlo de 11:

resultado= 11-resultado

#6)Finalmente, el dígito verificador será el obtenido en la resta: 201012341-3.
print(numero-resultado)