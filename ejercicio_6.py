# Ejercicio 6: Clasificador de Números
# Objetivo: Crear un programa que reciba números y los clasifique como positivos pares, positivos impares o negativos.
# - Utilizar constantes, operadores y funciones para clasificar y mostrar el resultado.

# Constantes para los tipos de clasificación
POSITIVO_PAR = "POSITIVO_PAR"
POSITIVO_IMPAR = "POSITIVO_IMPAR"
NEGATIVO = "NEGATIVO"

# Función para clasificar los números
def clasificar_numero(numero):
    if numero < 0:
        return NEGATIVO
    elif numero > 0:
        if numero % 2 == 0:
            return POSITIVO_PAR
        else:
            return POSITIVO_IMPAR
    else:
        return "Cero (no clasificado)"
