#Ejercicio 16¶
#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue 
#el mayor número ingresado.

def leeNumero():
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return int(numero)

def numeroMayor():
    mayor = 0
    numero = leeNumero()
    while numero != 0:
        if numero > mayor:
            mayor = numero
        numero = leeNumero()
    return mayor

if __name__ == "__main__":
    print(numeroMayor())