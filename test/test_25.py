from src.ejercicio25 import palabraLarga, numeroPalabrasLargas

def test_25():
    assert palabraLarga(["hola", "buenas", "noches"]) == "buenas"
    assert numeroPalabrasLargas(["hola", "buenas", "noches"]) == 2