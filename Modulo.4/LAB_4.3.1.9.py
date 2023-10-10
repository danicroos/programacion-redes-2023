'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  09-oct-2023
Descripcion: 
'''
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
