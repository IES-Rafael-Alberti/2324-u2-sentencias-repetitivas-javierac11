#Ejercicio 6¶
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
#rectángulo como el de más abajo, de altura el número introducido.

def leeNumero():
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return int(numero)


def triangulo(numero):
    lista_triangulo = ""
    simbolo = "*"
    for i in range(1, numero+1):
        if i == numero:
            lista_triangulo += f"{simbolo*i}"
        else:
            lista_triangulo += f"{simbolo*i}\n"
    return lista_triangulo

if __name__ == "__main__":
    numero = leeNumero()
    print(triangulo(numero))