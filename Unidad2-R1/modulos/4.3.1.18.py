'''
Autor: Zuniga Olvera Jorge Daniel
lab: 3.4.1.18
fecha: 21-Nov-2023
'''
import os

def find(path, target_dir):
    for root, dirs, files in os.walk(path):
        if target_dir in dirs:
            print(os.path.abspath(os.path.join(root, target_dir)))

# Ejemplo
path = "./tree"
target_directory = "python"
find(path, target_directory)
