#Ejercicio 24¶
#Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1,
#finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.

def leeNumero() -> int:
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return int(numero)

def leerNumeros() -> list:
    numero = leeNumero()
    numeros = []
    while numero != 0:
        numeros.append(numero)
        numero = leeNumero()
    return numeros

def esPrimo(numero: int): 
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def cantidadPrimos(numeros: list) -> int:
    cont_primos = 0
    for numero in numeros:
        if esPrimo(numero):
            cont_primos += 1
    return cont_primos
    
if __name__ == "__main__":
    numeros = leerNumeros()
    print(cantidadPrimos(numeros))
    