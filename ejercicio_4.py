# Ejercicio 4: Generador de Siglas de Frases
# Objetivo: Crear un programa que genere la sigla de una frase ingresada, tomando la primera letra de cada palabra.
# - Convertir cada inicial a mayúsculas y devolver la sigla completa.

# Función para generar las siglas de una frase
def generar_sigla(frase):
    # Dividir la frase en palabras y tomar la primera letra de cada palabra
    palabras = frase.split()
    siglas = ''.join([palabra[0].upper() for palabra in palabras])
    return siglas
