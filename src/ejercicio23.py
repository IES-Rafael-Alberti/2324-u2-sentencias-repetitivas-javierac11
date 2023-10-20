#Ejercicio 23¶
#Crear un programa que permita al usuario ingresar títulos de libros por teclado, 
# finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario 
# ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea.
# Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total 
# (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas
# completas se ingresaron.
'''
Ejemplo de ejecución:
Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
Libro: /
Línea completa. Aparecen 2 dígitos numéricos.
Libro: 20000 leguas de viaje submarino
Libro: El señor de los anillos
Libro: /
Línea completa. Aparecen 5 dígitos numéricos.
Libro: 20 años después
Libro: *
Fin. Se leyeron 2 líneas completas.
'''

def calcularCantidadDigitos(linea: str):
    numeros = 0
    for letra in linea:
        if str.isnumeric(letra):
            numeros += 1
    return numeros

def nuevaLinea():
    linea = ""
    linea_input = input("Libro: ")
    if linea_input == "*":
        return "*"
    while linea_input != "/":
        if linea_input == "*":
            return "*"
        else:
            linea += linea_input
            linea_input = input("Libro: ")
    return linea
    
if __name__ == "__main__":
    
    lineas = 0
    linea = nuevaLinea()
    
    while linea != "*":
        print(f"Línea completa. Aparecen {calcularCantidadDigitos(linea)} dígitos numéricos.")
        linea = nuevaLinea()
        lineas += 1
        
    print("Fin. Se leyeron 2 líneas completas.")
