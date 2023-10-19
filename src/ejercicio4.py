#Ejercicio 4¶
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la 
#cuenta atrás desde ese número hasta cero separados por comas.

#ENTRADA

def leeNumero():
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return int(numero)

#PROCESO

def cuentaAtras(numero):
    cuenta_atras = ""
    for i in range(numero, -1, -1):
        cuenta_atras += f"{i}"
        if i != 0:
            cuenta_atras += ", "
    return cuenta_atras
    
#SALIDA
    
if __name__ == "__main__":   
    numero = leeNumero()
    print(cuentaAtras(numero))