#Ejercicio 19¶
#Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa.
# A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, 
# informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo
# volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá 
# la impresión del menú y el programa finalizará.

def menu():
    numero = input("1- comenzar programa\n2- imprimir listado\n3-finalizar programa\n")
    while numero != "3":
        if numero == "1":
            print("Comenzando programa...")
            numero = input("1- comenzar programa\n2- imprimir listado\n3-finalizar programa\n")
        elif numero == "2":
            print("Listado: 1, 3, 5")
            numero = input("1- comenzar programa\n2- imprimir listado\n3-finalizar programa\n")
        else: 
            print("ERROR. SELECCIONE OPCION CORRECTA")
            numero = input("1- comenzar programa\n2- imprimir listado\n3-finalizar programa\n")            
            
if __name__ == "__main__":
    menu()