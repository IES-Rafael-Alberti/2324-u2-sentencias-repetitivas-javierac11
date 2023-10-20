#Ejercicio 22¶
#Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario 
#ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. 
#Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

def leeNumeroStr() -> int:
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return numero

def leerNumerosStr() -> list:
    numeros = []
    numero = leeNumeroStr()
    while numero != "0":
        numeros.append(numero)
        numero = leeNumeroStr()
    return numeros

def esPar(numeros: list):
    cont = 0
    for numero in numeros:
        for digito in numero:
            if int(digito) % 2 == 0:
                cont += 1
    return cont

def esImpar(numeros: list):
    cont = 0
    for numero in numeros:
        for digito in numero:
            if int(digito) % 2 != 0:
                cont += 1
    return cont

if __name__ == "__main__":
    
    numeros = leerNumerosStr()
    pares = esPar(numeros)
    impares = esImpar(numeros)
    print(f"Pares = {pares}\nImpares = {impares}")