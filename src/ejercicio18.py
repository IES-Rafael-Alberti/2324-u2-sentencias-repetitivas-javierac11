#Ejercicio 18¶
#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los 
#dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar 
#cuántos de los números ingresados por el usuario fueron números pares.

def leeNumero():
    negativo = False
    numero = input("Introduce un numero: ")
    if numero == "-1":
        negativo = True
        numero = "1"
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
        if numero == "-1":
            negativo = True
            numero = "1"
        else:
            negativo = False
    if negativo:
        numero = "-"+numero
    return int(numero)


def leerNumeros() -> list:
    numero = leeNumero()
    numeros = []
    while numero != -1:
        numeros.append(numero)
        numero = leeNumero()
    return numeros

def numerosPares(numeros: list) -> list:
    pares = []
    for i in numeros:
        if i % 2 == 0:
            pares.append(i)
    return pares

if __name__ == "__main__":

    numeros = leerNumeros()
    print(numerosPares(numeros))