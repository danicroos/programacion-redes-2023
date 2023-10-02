'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  02-oct-2023
Descripcion: 
'''
print("Ingresa cantidad")
n = input()
def calcular_impuesto(cantidad):
    if cantidad <= 0:
        return "La cantidad debe ser mayor a cero."
    if cantidad < 10000:
        impuesto = cantidad * 0.05  
    elif cantidad < 20000:
        impuesto = cantidad * 0.15  
    elif cantidad < 35000:
        impuesto = cantidad * 0.20  
    elif cantidad < 60000:
        impuesto = cantidad * 0.30  
    else:
        impuesto = cantidad * 0.45  
    return impuesto

print(calcular_impuesto (int(n)))