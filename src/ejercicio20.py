#Ejercicio 20¶
#Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase).
#Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide,
#indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra
#una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.

def leeLetra():
    letra = input("Introduce una letra: ")
    while len(letra) != 1:
        letra = input("ERROR.Introduce una letra: ")
    return letra

def leeFrase(mensaje: str):
    palabra = input(mensaje)
    return palabra

def buscarLetra(frase, letra):
    cont = 0
    salida = ""
    for i in frase:
        if i != letra:
            salida += f"{cont}, no esta\n"
        else:
            salida += f"{cont}, esta"
            return salida
        cont += 1
    return salida

if __name__ == "__main__":
    frase = leeFrase("Introduce una frase: ")
    letra = leeLetra()
    print(buscarLetra(frase, letra))