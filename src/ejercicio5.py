#Ejercicio 5¶
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
#el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que 
#dura la inversión.
# Formula para calcular El capital tras un año.
# amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 

def calcularInversion(cantidad, interes, anios):
    total = cantidad 
    for _ in range(0, anios):
        total *= 1 + interes / 100
        print(total)
   
if __name__ == "__main__": 
    cantidad = int(input("Introduce la cantidad a invertir: "))
    interes = int(input("Introduce el interes: "))
    anios = int(input("Introduce los años: "))
    calcularInversion(cantidad, interes, anios)