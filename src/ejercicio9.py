#Ejercicio 9¶
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def contrasenia(contrasenia):
    contrasenia_input = input("Introduce la contraseña: ")
    while contrasenia != contrasenia_input:
        contrasenia_input = input("Contraseña invalida. Intorduce la contraseña: ")
    
    return "contraseña correcta"

if __name__ == "__main__":
    print(contrasenia("12345"))