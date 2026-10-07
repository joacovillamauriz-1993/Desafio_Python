import operaciones

def test_suma_1():
    """valida que la suma de los argumentos entregados sea correcta"""
    assert operaciones.suma(50, 0) == 100

def test_suma_2():
    """valida que la suma de los argumentos entregados sea correcta"""
    assert operaciones.suma(100, 20) == 120