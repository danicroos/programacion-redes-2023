'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  02-oct-2023
Descripcion: 
'''
sombrero = [1, 2, 3, 4, 5]

# Paso 1: Reemplazar el número central en la lista
num_central = int(input("Ingresa un número entero para reemplazar el número central: "))
sombrero[2] = num_central

# Paso 2: Eliminar el último elemento de la lista
del sombrero[-1]

# Paso 3: Imprimir la longitud de la lista
longitud = len(sombrero)
print("La longitud de la lista es:", longitud)