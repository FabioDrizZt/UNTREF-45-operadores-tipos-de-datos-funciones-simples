edad = input("Ingrese su edad: ")
if edad.isdigit():
  edad = int(edad)
  if edad >= 18:
    print("Es mayor de edad")
    print("Puede votar")
  elif 13<= edad < 18:
    print("Es adolescente")
  elif edad>0:
    print("Es un niño")
else:
  print("Edad no valida")

# Metodos de String
nombre_usuario = input("Ingrese su nombre de usuario: ")
if nombre_usuario.strip().lower() == "fabio":
  print("Bienvenido Fabio!")
else: 
  print("Usted no es fabio =(")