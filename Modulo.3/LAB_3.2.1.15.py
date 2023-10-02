'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  02-oct-2023
Descripcion: 
'''
def collatz(n):
    steps = 0
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    print(n)
    return steps

numero = int(input("Ingresa un número natural: "))
pasos = collatz(numero)
print("Se necesitaron", pasos, "pasos para llegar al valor 1.")