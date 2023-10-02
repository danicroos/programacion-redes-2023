'''
    Nombre:     Daniel Zuñiga
    Fecha:      18-sep-2023
    Descripcion:
    Laboratorio:
'''
# Ingresa un valor flotante para la variable a
a = float(input("Ingresa un valor flotante para la variable a: "))

# Ingresa un valor flotante para la variable b
b = float(input("Ingresa un valor flotante para la variable b: "))

# Muestra el resultado de la suma
suma = a + b
print("La suma es:", suma)

# Muestra el resultado de la resta
resta = a - b
print("La resta es:", resta)

# Muestra el resultado de la multiplicación
multiplicacion = a * b
print("La multiplicación es:", multiplicacion)

# Muestra el resultado de la división
if b != 0:
  division = a / b
  print("La división es:", division)
else:
  print("No se puede dividir entre cero")

print("\n¡Eso es todo, amigos!")