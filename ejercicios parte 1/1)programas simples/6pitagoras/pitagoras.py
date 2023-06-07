#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.
ca= int(input("Ingrese el cateto a: "))
cb= int(input("Ingrese el cateto b: "))

hipotenusa=(ca**2+cb**2)**(1/2)
print(f"La hipotenusa es: {hipotenusa}")
