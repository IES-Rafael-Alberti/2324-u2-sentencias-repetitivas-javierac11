#Ejercicio 25¶
#Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga 
#(en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: 
#se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

def leeFraseSeparada() -> list:
    frase = input("Introduce una frase: ")
    frase = frase.split(" ")
    return frase

def palabraLarga(frase_separada: list) -> str:
    palabra_larga = ""
    for palabra in frase_separada:
        if  len(palabra) > len(palabra_larga):
            palabra_larga = palabra
    return palabra_larga
    
def numeroPalabrasLargas(frase_separada: list) -> int:
    palabra_larga = ""
    cont_palabras = 0
    for palabra in frase_separada:
        if  len(palabra) > len(palabra_larga):
            palabra_larga = palabra
            cont_palabras = 1
        elif len(palabra) == len(palabra_larga):
            cont_palabras += 1    
    return cont_palabras 

if __name__ == "__main__":
    frase = leeFraseSeparada()
    print(palabraLarga(frase))
    print(numeroPalabrasLargas(frase))