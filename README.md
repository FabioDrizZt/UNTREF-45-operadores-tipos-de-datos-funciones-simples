# Ejercicios de Python - Clase 2

Estos ejercicios están diseñados para desafiar a estudiantes con experiencia en otros lenguajes a aplicar conceptos de Python, incluyendo variables, constantes, operadores, condicionales y funciones.

## Lista de Ejercicios

1. **Simulador de Conversor de Unidades**
   - Crear un programa que convierta entre unidades de temperatura (Celsius, Fahrenheit) y longitud (metros, pies).

2. **Validador de Contraseñas**
   - Crear un programa que valide si una contraseña cumple con requisitos específicos de longitud, tipo de caracteres y espacios.

3. **Calculadora de Descuentos por Edad y Membresía**
   - Crear un programa que calcule el precio de una entrada de cine considerando descuentos por edad y membresía.

4. **Generador de Siglas de Frases**
   - Crear un programa que genere la sigla de una frase ingresada, tomando la primera letra de cada palabra.

5. **Juego de Adivinanza con Pistas Numéricas**
   - Crear un juego en el que el usuario debe adivinar un número entre 1 y 100, recibiendo pistas en base a la cercanía.

6. **Clasificador de Números**
   - Crear un programa que reciba números y los clasifique como positivos pares, positivos impares o negativos.

# Instrucciones para Ejecutar Pruebas

Este proyecto incluye pruebas automatizadas para verificar que cada ejercicio esté implementado correctamente. A continuación, te explicamos cómo configurar el entorno de pruebas y ejecutar los tests.

## Requisitos

Asegúrate de tener `pytest` instalado en tu entorno de Python. Puedes instalarlo usando el siguiente comando:

```bash
pip install pytest
```

## Ejecución de Pruebas
1. Ubica el archivo de pruebas: Guarda el archivo test_ejercicios.py en el mismo directorio que los archivos de ejercicios (como ejercicio_1.py, ejercicio_2.py, etc.).

2. Ejecuta las pruebas: En la terminal, navega al directorio del proyecto y ejecuta el siguiente comando:

```bash
pytest test_ejercicios.py
```

## Resultados de las pruebas:

- Si todos los ejercicios están implementados correctamente, verás un mensaje de éxito para cada prueba.
- En caso de errores, pytest te mostrará en qué pruebas falló, ayudándote a identificar qué ejercicios requieren ajustes.
  
## Notas Importantes
- Asegúrate de que cada archivo de ejercicio tenga las funciones requeridas y que el nombre de las funciones coincida con los especificados en el archivo de prueba.
- Los mensajes de error de pytest te ayudarán a depurar y mejorar el código.
