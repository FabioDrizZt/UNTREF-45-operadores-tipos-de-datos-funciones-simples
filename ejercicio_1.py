# Ejercicio 1: Simulador de Conversor de Unidades
# Objetivo: Crear un programa que convierta entre unidades de temperatura (Celsius, Fahrenheit) y longitud (metros, pies).
# - Solicitar al usuario la unidad de entrada y el valor a convertir.
# - Convertir entre Celsius y Fahrenheit, y entre metros y pies.
# - Usar funciones para cada tipo de conversión.
# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Función para convertir Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Función para convertir metros a pies
def metros_a_pies(metros):
    return metros * 3.28084

# Función para convertir pies a metros
def pies_a_metros(pies):
    return pies / 3.28084

# Función principal que solicita la conversión y muestra el resultado
def conversor_unidades():
    tipo_conversion = input("¿Qué tipo de conversión quieres hacer? (temperatura/longitud): ").strip().lower()

    if tipo_conversion == "temperatura":
        unidad_entrada = input("¿Cuál es la unidad de entrada? (Celsius/Fahrenheit): ").strip().lower()
        valor = float(input("Ingresa el valor a convertir: "))

        if unidad_entrada == "celsius":
            resultado = celsius_a_fahrenheit(valor)
            print(f"{valor} °C son {resultado:.2f} °F")
        elif unidad_entrada == "fahrenheit":
            resultado = fahrenheit_a_celsius(valor)
            print(f"{valor} °F son {resultado:.2f} °C")
        else:
            print("Unidad no reconocida. Intenta con 'Celsius' o 'Fahrenheit'.")

    elif tipo_conversion == "longitud":
        unidad_entrada = input("¿Cuál es la unidad de entrada? (metros/pies): ").strip().lower()
        valor = float(input("Ingresa el valor a convertir: "))

        if unidad_entrada == "metros":
            resultado = metros_a_pies(valor)
            print(f"{valor} metros son {resultado:.2f} pies")
        elif unidad_entrada == "pies":
            resultado = pies_a_metros(valor)
            print(f"{valor} pies son {resultado:.2f} metros")
        else:
            print("Unidad no reconocida. Intenta con 'metros' o 'pies'.")

    else:
        print("Tipo de conversión no reconocida. Intenta con 'temperatura' o 'longitud'.")

