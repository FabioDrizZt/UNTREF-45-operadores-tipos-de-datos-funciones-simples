# Ejercicio 5: Juego de Adivinanza con Pistas Numéricas
# Objetivo: Crear un juego en el que el usuario debe adivinar un número entre 1 y 100, recibiendo pistas en base a la cercanía.
# - El juego termina cuando el usuario adivina correctamente, usando funciones y condicionales.
import random

# Función para verificar si el número es muy alto o muy bajo
def verificar_adivinanza(intentos):
    # Número secreto predefinido para las pruebas
    numero_secreto = 50  # Puedes cambiar este valor para el test
    if intentos < numero_secreto:
        return "muy bajo"
    elif intentos > numero_secreto:
        return "muy alto"
    else:
        return "adivinado"