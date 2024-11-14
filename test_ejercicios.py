import pytest # type: ignore
from ejercicio_1 import celsius_a_fahrenheit, fahrenheit_a_celsius, metros_a_pies, pies_a_metros
from ejercicio_2 import validar_contraseña
from ejercicio_3 import calcular_precio_final
from ejercicio_4 import generar_sigla
from ejercicio_5 import verificar_adivinanza
from ejercicio_6 import clasificar_numero

# Ejercicio 1: Simulador de Conversor de Unidades
def test_ejercicio_1():
    assert celsius_a_fahrenheit(0) == 32
    assert fahrenheit_a_celsius(32) == 0
    assert metros_a_pies(1) == pytest.approx(3.281, 0.01)
    assert pies_a_metros(3.281) == pytest.approx(1, 0.01)

# Ejercicio 2: Validador de Contraseñas
def test_ejercicio_2():
    assert validar_contraseña("Aa1bcdef") == True
    assert validar_contraseña("abcdef") == False
    assert validar_contraseña("Abcdefg") == False
    assert validar_contraseña("abc 12345") == False

# Ejercicio 3: Calculadora de Descuentos por Edad y Membresía
def test_ejercicio_3():
    assert calcular_precio_final(17, False) == pytest.approx(85, 0.01)  # 15% descuento
    assert calcular_precio_final(61, False) == pytest.approx(70, 0.01)  # 30% descuento
    assert calcular_precio_final(61, True) == pytest.approx(60, 0.01)   # 30% + 10% descuento

# Ejercicio 4: Generador de Siglas de Frases
def test_ejercicio_4():
    assert generar_sigla("Python es genial") == "PEG"
    assert generar_sigla("Machine Learning Avanzado") == "MLA"
    assert generar_sigla("Data Science") == "DS"

# Ejercicio 5: Juego de Adivinanza con Pistas Numéricas
def test_ejercicio_5():
    assert verificar_adivinanza(50) == "muy alto" or "muy bajo"  # Adjust based on secret number used in the function

# Ejercicio 6: Clasificador de Números
def test_ejercicio_6():
    assert clasificar_numero(10) == "POSITIVO_PAR"
    assert clasificar_numero(-3) == "NEGATIVO"
    assert clasificar_numero(7) == "POSITIVO_IMPAR"
