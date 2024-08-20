from typing import List

def promedio(lista: List[float])-> float:
    if len(lista) == 0:
        return 0
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)
    
print(promedio([7.0, 3.1, 1.7]))
print(promedio([1,4,9,16]))

def cuadrados(lista: List[float]) -> List[float]:
    listaCuadrados: List[float] = []
    for i in lista:
        listaCuadrados.append(i**2)
    return listaCuadrados

print(cuadrados([1, 2, 3, 4, 5]))
print(cuadrados([3.4, 1.2]))


def masLargo(palabras: List[str]) -> str:
    max = ""
    for i in palabras:
        if (len(i) > len(max)):
            max = i
    return max
print(masLargo(['raton', 'hipopotamo', 'buey', 'jirafa']))
print(masLargo(['****', '**', '********', '**']))
      