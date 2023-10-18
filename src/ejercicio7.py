#Ejercicio 7¶
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tablaMultiplicar():
    for x in range(1, 11):
        for i in range(1, 11):
            print(f"{x} * {i} = {x*i}")
        print("--------------")

if __name__ == "__main__":
    tablaMultiplicar()