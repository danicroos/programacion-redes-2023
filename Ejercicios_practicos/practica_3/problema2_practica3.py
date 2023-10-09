'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  09-oct-2023
Descripcion: practica 3
'''

lstnombres = []
for i in range(5):
    nombre = input("Ingrese el nombre de un amigo o amiga: ")
    lstnombres.append(nombre)
    
lstedades = []
for i in range(5):
    edad = int(input("Ingrese la edad de su amigo o amiga: "))
    lstedades.append(edad)

dicDatos = {}
for i in range(len(lstnombres)):
    dicDatos[lstnombres[i]] = lstedades[i]

def desplegar_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(clave, "->", valor)

desplegar_diccionario(dicDatos)

print("La longitud de lstnombres es:", len(lstnombres))
print("La longitud de lstedades es:", len(lstedades))
print("La longitud de dicDatos es:", len(dicDatos))

claves_ordenadas = sorted(dicDatos.keys())
print("Las claves ordenadas son:", claves_ordenadas)

def buscar_valor(diccionario, clave):
    if clave in diccionario:
        return diccionario[clave]
    else:
        return None

clave_buscar = input("Ingrese la clave a buscar: ")
valor_encontrado = buscar_valor(dicDatos, clave_buscar)
print("El valor encontrado es:", valor_encontrado)
