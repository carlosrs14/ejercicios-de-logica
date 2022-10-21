#Escriba un programa que muestre una tabla de multiplicar 10 x 10:
#los número deben estar alineados a la derecha
for i in range(1, 11):
    for s in range(1,11):
        if(len(str(s*i))==1):
            print("  ",s*i, end="")
        elif(len(str(s*i))==2):
            print(" ",s*i, end="")
        elif(len(str(s*i))==3):
            print("",s*i, end="")
    
    print("")