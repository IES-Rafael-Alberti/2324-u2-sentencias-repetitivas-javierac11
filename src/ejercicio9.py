#Ejercicio 9¶
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

def leeContrasenia() -> str:
    contrasenia = input("Introduce la contraseña: ")
    return contrasenia
    
def compruebaContrasenia(contrasenia, contrasenia_input) -> bool:
    if contrasenia == contrasenia_input:
        return True
    else:
        return False
    
def contrasenia(contrasenia) -> str:
    contrasenia_input = leeContrasenia()
    while not compruebaContrasenia(contrasenia, contrasenia_input):
        contrasenia_input = leeContrasenia()
    return "contraseña correcta"

if __name__ == "__main__":
    print(contrasenia("12345"))