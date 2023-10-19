#Ejercicio 7¶
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tablaMultiplicar():
    tabla = ""
    for x in range(1, 11):
        for i in range(1, 11):
            tabla += f"{x} * {i} = {x*i}\n"
        tabla += "--------------\n"
    return tabla

if __name__ == "__main__":
    print(tablaMultiplicar())