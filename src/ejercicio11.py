#Ejercicio 11¶
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las 
# letras de la palabra introducida empezando por la última.

def letraAlReves(palabra):
    
    palabra_al_reves = []
    
    for letra in palabra[::-1]:
        palabra_al_reves.append(letra)
    return palabra_al_reves
        
if __name__ == "__main__":
    palabra = input("Introduce una palabra: ")
    palabra_al_reves = letraAlReves(palabra)
    for letra in palabra_al_reves:
        print(letra)

    