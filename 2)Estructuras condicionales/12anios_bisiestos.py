#Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:
anio = int(input("Ingrese el año actual: "))
isbisiesto=False
if(anio > 1582):
    if(anio%4==0):
        isbisiesto = True
    
    if(anio%100==0):
        isbisiesto=False
        if(anio%400==0):
            isbisiesto= True
            
else:
    if(anio%4==0):
        isbisiesto = True


if (isbisiesto):
    print(f"{anio} es biciesto")
else:
    print(f"{anio} no es biciesto")