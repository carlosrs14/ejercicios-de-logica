#Escriba un programa que simule una calculadora básica, este puede realizar operación de suma, resta, multiplicación y división.
print("Calculadora\n")
print("Se puede usar +, -, *, /, **\n")
numero1 = int(input("Ingresa el primer número: "))
operador= input("ingrese el operador: ")
numero2 = int(input("Ingresa el segundo número: "))

if (operador=="+"):
    print(f"{numero1} + {numero2} = {numero1+numero2}")
elif (operador=="-"):
    print(f"{numero1} - {numero2} = {numero1-numero2}")
elif (operador=="*"):
    print(f"{numero1} * {numero2} = {numero1*numero2}")
elif (operador=="/"):
    print(f"{numero1} / {numero2} = {numero1/numero2}")
elif (operador=="**"):
    print(f"{numero1} ^ {numero2} = {numero1**numero2}")