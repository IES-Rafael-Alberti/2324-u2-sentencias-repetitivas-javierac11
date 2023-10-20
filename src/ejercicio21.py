#Ejercicio 21¶
#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
# (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo,
# no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a 
# pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

def leeNumero() -> int:
    numero = input("Introduce un numero: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
    return int(numero)

def calcularDescuento(monto: int) -> bool:
    if monto > 1000:
        return 10
    else:
        return 0

def aniadirMontos():
    montos = 0
    monto = leeNumero()
    while monto != 0:
        montos += monto
        monto = leeNumero()
    return montos
    
def calcularPorcentaje(numero, porcentaje):
    descuento = numero * (porcentaje/100)
    total = numero - descuento
    return total

if __name__ == "__main__":
    total = aniadirMontos()
    porcentaje = calcularDescuento(total)
    print(calcularPorcentaje(total, porcentaje))