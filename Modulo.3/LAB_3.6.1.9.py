'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  02-oct-2023
Descripcion: 
'''
lista_original = [1, 2, 3, 2, 4, 5, 3, 6, 2, 7, 8, 9, 1, 5]

lista_sin_repeticiones = []

for numero in lista_original:
    if numero not in lista_sin_repeticiones:
        lista_sin_repeticiones.append(numero)

print(lista_sin_repeticiones)