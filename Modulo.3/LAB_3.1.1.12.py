'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  02-oct-2023
Descripcion: 
'''
year = int(input("Ingrese un año: "))

if year < 1582:
    print("No dentro del período del calendario Gregoriano")
else:
    if year % 4 != 0:
        print("Año Común")
    elif year % 100 != 0:
        print("Año Bisiesto")
    elif year % 400 != 0:
        print("Año Común")
    else:
        print("Año Bisiesto")