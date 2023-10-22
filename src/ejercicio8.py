#Ejercicio 8¶
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
#rectángulo como el de más abajo.

def leeNumero():
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return int(numero)

def trianguloImpar(numero):
    numeros_impares = ""
    numeros = [1]
    numero_impar = 1
    for x in range(0, numero):
        
        for num in numeros:
            numeros_impares += f"{num} "
        if x == numero-1:
            pass
        else:
            numeros_impares += "\n"
        numero_impar += 2
        numeros.insert(0, numero_impar)
    return numeros_impares

if __name__ == "__main__":
    numero = leeNumero()
    print(trianguloImpar(numero))