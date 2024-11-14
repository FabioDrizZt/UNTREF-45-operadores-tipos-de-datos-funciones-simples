# Ejercicio 2: Validador de Contraseñas
# Objetivo: Crear un programa que valide si una contraseña cumple con requisitos específicos de longitud, tipo de caracteres y espacios.
# - Tener al menos 8 caracteres, incluir mayúsculas, minúsculas y un número, sin espacios en blanco.
# - Utilizar condicionales, funciones y operadores para validar.

import re

# Función para validar si una contraseña cumple con los requisitos
def validar_contraseña(contraseña):
    # Verificar longitud mínima
    if len(contraseña) < 8:
        return False
    
    # Verificar que no tenga espacios
    if " " in contraseña:
        return False
    
    # Inicializar banderas para verificar tipos de caracteres
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    
    # Verificar que tenga al menos una mayúscula, una minúscula y un número
    tiene_mayuscula = re.search(r'[A-Z]', contraseña) is not None # any(c.isupper() for c in contraseña)
    tiene_minuscula = re.search(r'[a-z]', contraseña) is not None # any(map(str.islower, contraseña))
    tiene_numero = re.search(r'\d', contraseña) is not None

    # Verificar que tenga al menos una mayúscula, una minúscula y un número
    if not tiene_mayuscula or not tiene_minuscula or not tiene_numero:
        return False
    
    # Si cumple con todos los requisitos
    return True

