#1)Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:
#2)Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:
#3)Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:
"""
alto = int(input("Ingresa el alto: "))
ancho = int(input("Ingresa el ancho: "))

for i in range(1,alto+1):
    print("*"*ancho)

alto = int(input("\nIngresa el alto: "))
for i in range(1,alto+1):
    print("*"*i)

"""
lado = int(input("\nIngresa el lado: "))
cont=1
for i in range(1,lado*2):
    if(i<=lado):
        print(" "*(lado-i),"*"*(lado+(cont-1)))
        cont+=2
    else:
        print(" "*(i-4),"*"*cont)
        cont-=2
    if (i==lado):
        cont=cont-1



