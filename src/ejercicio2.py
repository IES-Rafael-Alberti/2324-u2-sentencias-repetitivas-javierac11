#Ejercicio 2¶
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años
#que ha cumplido (desde 1 hasta su edad).

def leeNumero():
    numero = input("Introduce los años: ")
    while not numero.isnumeric():
        numero = input("ERROR.Introduce los años: ")
    return int(numero)

def aniosCumplidos(anios: int):
    anios_ = ""
    for i in range(1, anios+1):
        if i == anios:
            anios_ += f"{i}"        
        else:
            anios_ += f"{i}\n"
    return anios_
    
if __name__ == "__main__":       
    anios = leeNumero()
    print(aniosCumplidos(anios))
