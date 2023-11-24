'''
Autor: Zuñiga Olvera Jorge Daniel
lab: 2.8.1.4
fecha: 20-Nov-2023
'''
def read_int(prompt, min, max):
    while True:
        try:
            entrada = int(input(prompt))
            if min <= entrada <= max:
                return entrada
        except ValueError:
            pass
        print(f"Error: {'entrada incorrecta' if not min <= entrada <= max else f'el valor no está dentro del rango permitido ({min}..{max})'}")

v = read_int("Ingresa un número entre -10 y 10: ", -10, 10)
print("El número es:", v)