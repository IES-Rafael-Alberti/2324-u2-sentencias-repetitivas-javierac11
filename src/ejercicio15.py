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

def leerNumeros() -> list:
    numeros = []
    numero = leeNumero()
    while numero != 0:
        numeros.append(numero)
        numero = leeNumero()
    return numeros

def sumarNumeros(numeros: list) -> int:
    suma = 0
    for numero in numeros:
        if numero > 0:
            suma += numero
    return suma


if __name__ == "__main__":
    numeros = leerNumeros()
    print(sumarNumeros(numeros))
    