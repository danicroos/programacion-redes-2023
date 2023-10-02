'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  02-oct-2023
Descripcion: 
'''
asignaturas = [
    "Probabilidad y Estadística",
    "Electrónica para IDC Física",
    "Conexión de redes WAN",
    "Administración de servidores I",
    "Programación de Redes",
    "Inglés IV"
]

notas = []

for asignatura in asignaturas:
    nota = input(f"Ingrese la nota de la unidad I de {asignatura}: ")
    notas.append(nota)

print("Notas del cuarto cuatrimestre:")
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")