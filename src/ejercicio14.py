#Ejercicio 14¶
#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente,
#mostrar la sumatoria de todos los números ingresados.

def leeNumero():
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return int(numero)

def sumarBucle():
    suma = 0
    numero = leeNumero()
    while numero != 0:
        suma += numero
        numero = leeNumero()
    return suma

if __name__ == "__main__":
    print(sumarBucle())
    
