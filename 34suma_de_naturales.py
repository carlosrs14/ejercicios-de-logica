nfinal = int(input("Ingrese n: "))
s1=0
s2=0

for i in range(1,nfinal+1):
    s1+=i
print(f"S1: {s1} ")

s2 = nfinal*(nfinal+1)//2
print(f"S2: {s2}")

if(s1==s2):
    print("Son iguales")
else:
    print("Son iguales")