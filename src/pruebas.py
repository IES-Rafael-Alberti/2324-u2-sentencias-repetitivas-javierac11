def leeNumero():
    negativo = False
    numero = input("Introduce un numero: ")
    if numero[0] == "-":
        negativo = True
        numero = numero[1:]
    while not numero.isnumeric():
        numero = input("ERROR.Introduce un numero: ")
        if numero[0] == "-":
            negativo = True
            numero = numero[1:]
        else:
            negativo = False
    if negativo:
        numero = "-"+numero
    return int(numero)
print(leeNumero())