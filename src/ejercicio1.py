#Ejercicio 1¶
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def repitePalabra(palabra, numero: int):
    cont = 0
    while cont < numero:
        print(palabra)
        cont += 1
        
if __name__ == "__main__":
    palabra = input("Introduce una palabra: ")
    numero = int(input("Introduce un numero: "))
    repitePalabra(palabra, numero)