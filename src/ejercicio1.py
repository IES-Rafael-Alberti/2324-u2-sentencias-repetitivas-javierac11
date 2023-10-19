#Ejercicio 1¶
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def leePalabra(mensaje: str):
    palabra = input(mensaje)
    return palabra

def leeNumero():
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return int(numero)

def repitePalabra(palabra: str, numero: int) -> str:
    cont = 0
    palabras = ""
    while cont < numero:
        if cont == numero-1:
            palabras += f"{palabra}"
        else:
            palabras += f"{palabra}\n"
        cont += 1
    return palabras
    
if __name__ == "__main__":
    palabra = leePalabra("Introduce una palabra: ")
    numero = leeNumero()
    print(repitePalabra(palabra, numero))