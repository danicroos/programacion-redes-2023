'''
Autor:  Zuñiga Olvera Jorge Daniel
Fecha:  02-oct-2023
Descripcion: 
'''
user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    if letter in ['A', 'E', 'I', 'O', 'U']:
        continue
    word_without_vowels += letter

print(word_without_vowels)