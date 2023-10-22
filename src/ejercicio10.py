#Ejercicio 10¶
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un
#número primo o no.

def leeNumero():
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return int(numero)

def esPrimo(numero): 
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

if __name__ == "__main__":
    
    numero = leeNumero()
    
    if esPrimo(numero):
        print("Es primo")
    else:
        print("No es primo")
