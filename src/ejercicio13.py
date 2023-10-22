#Ejercicio 13¶
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario
#escriba “salir” que terminará.

def compruebaPalabra(frase, fin):
    if frase == fin:
        return False
    else:
        return True
    
if __name__ == "__main__":

    fin = "salir"
    frase = input(f"Introduzca lo que sea, si introduces \"salir\" terminara: ")
    while compruebaPalabra(frase, fin) == True:
        print(frase)
        frase = input(f"Introduzca lo que sea, si introduces \"salir\" terminara: ")
