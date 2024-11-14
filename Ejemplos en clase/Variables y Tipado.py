# Definición de variables
nombre = "Fabio"
año_actual = 2024
año_nacimiento = 1988
edad_calculada = año_actual - año_nacimiento
altura = 1.69
es_profesor = True
salario = None

# Tipos de datos
print(type(nombre))
print(type(edad_calculada))
print(type(altura))
print(type(es_profesor))
print(type(salario))

# Formas de hacer print
print(f"Mi edad es {edad_calculada}, mi altura es: {altura}")
print("Mi nombre es " + nombre + ", mi edad es: ", edad_calculada)

# CONSTANTES
PI = 3.141516
GRAVEDAD = 9.80665
MAX_CONNECTIONS = 100

es_string = isinstance(nombre, str)
es_int = isinstance(año_actual, int)