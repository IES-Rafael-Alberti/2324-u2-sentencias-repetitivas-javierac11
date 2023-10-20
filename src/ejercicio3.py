#Ejercicio 3¶
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
#todos los números impares desde 1 hasta ese número separados por comas.

def leeNumero():
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return int(numero)

def numerosImpares(numero: int):
    impares = ""
    if numero < 0:
        print("Error")
    else:
        for i in range(0, numero+1):
            if i%2 != 0:
                impares += f"{i}, "
    return impares
            
if __name__ == "__main__":       
    numero = leeNumero()
    print(numerosImpares(numero))