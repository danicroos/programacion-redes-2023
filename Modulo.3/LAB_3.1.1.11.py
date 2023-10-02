'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  25-sep-2023
Descripcion: 
'''
income = float(input("Introduce el ingreso anual:"))

#
# Escribe tu código aquí.
#
if income <= 85_528:
    tax = income * 0.18 -526.02

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")