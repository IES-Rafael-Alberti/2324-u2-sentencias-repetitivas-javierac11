#Ejercicio 4¶
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
#cuenta atrás desde ese número hasta cero separados por comas.

def cuentaAtras(numero):
    for i in range(numero, -1, -1):
        print(i, end="")
        if i != 0:
            print(", ", end="")
    print() 
    
if __name__ == "__main__":   
    numero = int(input("Introduce un numero: "))
    cuentaAtras(numero)