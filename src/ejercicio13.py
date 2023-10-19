#Ejercicio 13¶
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario
#escriba “salir” que terminará.

def repetir():
    entrada = input(f"Introduzca lo que sea, si introduces \"salir\" terminara: ")
    while entrada != "salir":
        print(entrada)
        entrada = input(f"Introduzca lo que sea, si introduces \"salir\" terminara: ")
     
if __name__ == "__main__":

    repetir()