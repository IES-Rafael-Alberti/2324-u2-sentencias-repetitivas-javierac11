#Ejercicio 8¶
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
#rectángulo como el de más abajo.

def trianguloImpar(numero):
    numeros = [1]
    numero_impar = 1
    for x in range(0, numero):
        for num in numeros:
            print(num, end=" ")
        print()
        numero_impar += 2
        numeros.insert(0, numero_impar)

if __name__ == "__main__":
    numero = int(input("Introduce un numero: "))
    trianguloImpar(numero)