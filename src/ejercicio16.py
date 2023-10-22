#Ejercicio 16¶
#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue 
#el mayor número ingresado.

def leeNumero():
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return int(numero)

def leerNumeros() -> list:
    numeros = []
    numero = leeNumero()
    while numero != 0:
        numeros.append(numero)
        numero = leeNumero()
    return numeros

def numeroMayor(numeros):
    mayor = 0
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor

if __name__ == "__main__":
    numeros = leerNumeros()
    print(numeroMayor(numeros))