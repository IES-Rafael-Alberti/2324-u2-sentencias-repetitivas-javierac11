#Ejercicio 10¶
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un
#número primo o no.

def esPrimo(numero): 
    for i in range(2, numero):
        if numero % i == 0:
            return "No es primo"
    return "Es primo"

if __name__ == "__main__":
    numero = int(input("introduce un numero: "))
    print(esPrimo(numero))