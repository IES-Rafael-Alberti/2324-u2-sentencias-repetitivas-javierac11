#Ejercicio 2¶
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años
#que ha cumplido (desde 1 hasta su edad).

def aniosCumplidos(anios):
    for i in range(1, anios+1):
        print(i)
 
if __name__ == "__main__":       
    anios = int(input("Introduce los años: "))
    aniosCumplidos(anios)