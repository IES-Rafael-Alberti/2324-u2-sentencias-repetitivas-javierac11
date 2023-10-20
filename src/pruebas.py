def numerosPares(numeros) -> list:
    pares = []
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
    return pares

print(numerosPares([1, 2, 3, 4, 5]))