#Ejercicio 3¶
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
#todos los números impares desde 1 hasta ese número separados por comas.

def numerosImpares(numero):
    if numero < 0:
        print("Error")
    else:
        for i in range(0, numero+1):
            
            if i%2 != 0:
                print(i, end=",")
        print()
        
if __name__ == "__main__":       
    numero = int(input("Introduce un numero: "))
    numerosImpares(numero)