a = 10
b = 5
# Operadores de comparación
print(a == b)
print(a < b)
print(a > b)
print(a != b)
print(a <= b)
print(a >= b)

edad = 16
es_adolescente = 13 < edad < 18

# Operadores Lógicos
es_mayor_de_edad = edad >= 16
tiene_dni = True
puede_votar = es_mayor_de_edad and tiene_dni
print(f"Puede votar? {puede_votar}")
print("Puede votar?", not puede_votar)

