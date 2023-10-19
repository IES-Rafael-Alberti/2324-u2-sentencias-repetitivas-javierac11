#Ejercicio 12¶
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.

def leeLetra():
    letra = input("Introduce una letra: ")
    while len(letra) != 1:
        letra = input("ERROR.Introduce una letra: ")
    return letra

def leePalabra(mensaje: str):
    palabra = input(mensaje)
    return palabra

def contarLetras(frase, letra):
    cont = 0
    for x in frase:
        if str.upper(x) == str.upper(letra):
            cont += 1 
    return cont

if __name__ == "__main__":
    
    palabra = leePalabra("Introduce una palabra: ")
    letra = leeLetra()
    
    print(contarLetras(palabra, letra))