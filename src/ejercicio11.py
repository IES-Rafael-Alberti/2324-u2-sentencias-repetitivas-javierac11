#Ejercicio 11¶
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las 
# letras de la palabra introducida empezando por la última.

def letraAlReves(palabra):
    for letra in palabra[::-1]:
        print(letra)
        
if __name__ == "__main__":
    palabra = input("Introduce una palabra: ")
    letraAlReves(palabra)