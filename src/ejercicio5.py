#Ejercicio 5¶
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y 
#el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que 
#dura la inversión.
# Formula para calcular El capital tras un año.
# amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual 

def isfloat(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

def leeNumero(mensaje):
    numero = input(mensaje)
    while not numero.isnumeric() and not isfloat(numero):
        numero = input(f"ERROR.{mensaje}")
    return float(numero)

def calcularInversion(cantidad, interes, anios):
    total = cantidad
    inversion = [] 
    for i in range(0, anios):
        total *= 1 + interes / 100
        inversion.append(total)
    return inversion
   
if __name__ == "__main__":
    cantidad = leeNumero("Introduce la cantidad a invertir: ")
    interes = leeNumero(("Introduce el interes: "))
    anios = int(leeNumero("Introduce los años: "))
    inversion = calcularInversion(cantidad, interes, anios) 
    
    for i in range(0, len(inversion)):
        print(f"Año {i+1} = {inversion[i]}")