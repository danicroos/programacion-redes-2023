'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  02-oct-2023
Descripcion: 
'''
num_bloques = int(input("Ingresa la cantidad de bloques: "))

altura_piramide = 0
bloques_disponibles = 0

while bloques_disponibles <= num_bloques:
    altura_piramide += 1
    bloques_disponibles += altura_piramide

    if bloques_disponibles > num_bloques:
        altura_piramide -= 1
        break

print("La altura de la pirámide es:", altura_piramide)