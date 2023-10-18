#Ejercicio 6¶
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
#rectángulo como el de más abajo, de altura el número introducido.

def triangulo(numero):
    for i in range(1, numero+1):
        print("*" * i)
        
if __name__ == "__main__":
    numero = int(input("Introduce un numero: "))
    triangulo(numero)