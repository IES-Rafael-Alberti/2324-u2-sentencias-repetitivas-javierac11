#Ejercicio 15¶
#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria
#de todos los números positivos ingresados.

def leeNumero():
    negativo = False
    numero = input("Introduce un numero: ")
    if numero[0] == "-":
        negativo = True
        numero = numero[1:]
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
        if numero[0] == "-":
            negativo = True
            numero = numero[1:]
        else:
            negativo = False
    if negativo:
        numero = "-"+numero
    return int(numero)

def sumarBuclePositivos():
    numeros = []
    suma = 0
    numero = leeNumero()
    while numero != 0:
        numeros.append(numero)
        numero = leeNumero()
    for num in numeros:
        if num > 0:
            suma += num 
    return suma

if __name__ == "__main__":
    print(sumarBuclePositivos())
    