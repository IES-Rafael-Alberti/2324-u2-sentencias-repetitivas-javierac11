#Ejercicio 17¶
#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.

def leeNumeroStr():
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return numero

def sumaDigitos(numero_str):
    suma = 0
    for digito in numero_str:
        suma += int(digito)
    return suma

if __name__ == "__main__":
    numero = leeNumeroStr()
    print(sumaDigitos(numero))