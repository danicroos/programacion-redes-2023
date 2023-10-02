'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  02-oct-2023
Descripcion: 
'''
# Paso 1: Crear una lista vacía llamada beatles
beatles = []

# Paso 2: Agregar los primeros miembros de la banda a la lista
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Paso 3: Pedir al usuario que agregue más miembros de la banda a la lista
for _ in range(2):
    miembro = input("Ingresa el nombre de un miembro de la banda: ")
    beatles.append(miembro)

# Paso 4: Eliminar a Stu Sutcliffe y Pete Best de la lista
del beatles[3:5]

# Paso 5: Agregar a Ringo Starr al principio de la lista
beatles.insert(0, "Ringo Starr")

# Imprimir la lista actualizada
print("La formación actual de los Beatles es:")
for miembro in beatles:
    print(miembro)
    