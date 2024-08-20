def mcd(n1: int, n2: int) -> int:
    minimo = min(n1, n2)
    for i in range(minimo + 1, 1, -1):
        if (n1 % i == 0 and n2 % i ==0):
            return i
    return 1
print(mcd(20, 50))
print(mcd(31, 19))