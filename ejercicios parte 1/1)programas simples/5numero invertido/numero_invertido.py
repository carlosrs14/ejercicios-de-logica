#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
def inverso(num):
    if(num<10):
        print(int(num))
    else:
        print(int(num%10), end="")
        inverso(num/10)

numero= int(input("Ingrese un número: "))
inverso(numero)


