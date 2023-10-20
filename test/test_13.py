from src.ejercicio13 import compruebaPalabra

def test_13():
    assert compruebaPalabra("hola", "salir") == True
    assert compruebaPalabra("salir", "salir") == False