from src.ejercicio21 import calcularDescuento, calcularPorcentaje

def test_21():
    assert calcularPorcentaje(1000, 10) == 900
    assert calcularDescuento(1001) == 10