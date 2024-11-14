def calcular_area_triangulo(base,altura):
  """ Calcula el area del triangulo """
  return base*altura/2

print(calcular_area_triangulo(2,4))

# Funciones anidadas
def calculadora(operacion, a, b):
  def suma(a,b):
    return a+b

  def multiplicacion(a,b):
    return a*b
  
  if operacion == 'suma':
   return suma(a,b)
  elif operacion == 'multiplicacion':
   return multiplicacion(a,b)
  else:
   return "Operacion invalida"

# ejemplos de uso
print(calculadora("suma", 5,6))
print(calculadora("multiplicacion", 5,6))