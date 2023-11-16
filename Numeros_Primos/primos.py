import math


inicio = int(input("Ingrese el número de inicio del rango: "))
fin = int(input("Ingrese el número de fin del rango: "))

primos = []

for numero in range(inicio, fin+1):
    if numero > 1:
        es_primo = True
        for i in range(2, int(math.sqrt(numero))+1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(numero)

print("Números primos en el rango dado: ", primos)
