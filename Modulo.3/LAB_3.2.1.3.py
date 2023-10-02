'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  02-oct-2023
Descripcion: 
'''
secret_number = 777
print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
while True:
    user_number = int(input("Ingresa un número entero: "))
    if user_number != secret_number:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    else:
        print("¡Bien hecho, muggle! Eres libre ahora")
        break