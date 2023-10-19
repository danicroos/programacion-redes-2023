'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  19-oct-2023
Descripcion: R1
'''
asignatura = {}

for clave in asignatura.keys():
    unidades = int(input(f"Ingrese el número de unidades temáticas {clave}: "))
    calificaciones = []
    for i in range(unidades):
        calificacion = int(input(f"Ingrese la calificación {i+1} de {clave}: "))
        calificaciones.append(calificacion)
    asignatura[clave] = calificaciones

def barra(calificacion):
    print("*" * calificacion)

def histograma(asignatura, calificaciones):
    print(f"{asignatura} histograma")
    for calificacion in calificaciones:
        barra(calificacion)

for asignatura, calificaciones in asignatura.items():
    histograma(asignatura, calificaciones)
directorio = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

lineas = directorio.split("\n")
campos = lineas[0].split(";")
clientes = {}

for linea in lineas[1:]:
    datos = linea.split(";")
    cliente = {}
    for i in range(len(campos)):
        campo = campos[i]
        valor = datos[i]
        cliente[campo] = valor
    clientes[datos[0]] = cliente

print(clientes)
