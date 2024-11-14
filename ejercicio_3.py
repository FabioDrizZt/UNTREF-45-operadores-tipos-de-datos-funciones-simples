# Ejercicio 3: Calculadora de Descuentos por Edad y Membresía
# Objetivo: Crear un programa que calcule el precio de una entrada de cine considerando descuentos por edad y membresía.
# - Aplica un descuento de 15% para menores de 18 años, 30% para mayores de 60 y 10% extra si es miembro del club.

# Función para calcular el precio con descuentos
def calcular_descuento(precio_base, edad, es_miembro):
    # Aplicar descuento según la edad
    if edad < 18:
        descuento = 0.15  # 15% para menores de 18 años
    elif edad > 60:
        descuento = 0.30  # 30% para mayores de 60 años
    else:
        descuento = 0  # Sin descuento para edades intermedias

    # Aplicar descuento adicional si es miembro
    if es_miembro:
        descuento += 0.10  # 10% adicional para miembros

    # Asegurarse de que no se apliquen más de un 100% de descuento
    if descuento > 1:
        descuento = 1
    
    # Calcular precio final
    precio_final = precio_base * (1 - descuento)
    return precio_final

# Función principal ajustada para aceptar parámetros y no usar input()
def calcular_precio_final(edad, es_miembro):
    precio_base = 100  # Asumimos que el precio base es 100 (puedes cambiarlo por un parámetro)
    # Calcular el precio con los descuentos aplicados
    precio_final = calcular_descuento(precio_base, edad, es_miembro)
    
    return precio_final
