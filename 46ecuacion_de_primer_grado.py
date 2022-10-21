#Escriba un programa que pida los coeficientes de una ecuación de primer grado:
#ax + b = 0, y que entregue la solución.
#Una ecuación de primer grado puede:
# tener solución única,
# tener infinitas soluciones, o
# no tener soluciones.

print("Tendrás un ecuación de este tipo : ax+b=0")
a=int(input("Ingresa el valor de a: "))
b=int(input("Ingresa el valor de b: "))
#despejar x

if(a==0 and b==0):
    print("No hay solución única")
elif(a==0):
    print("Sin solución")
else:
    print(f"Solución única: {-b/a}")