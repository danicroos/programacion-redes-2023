'''
Descripcion:Chuck Norris Joke API
Author: Zuñiga Olvera Jorge Daniel
Fecha: 16-11-2023
'''
import urllib.parse
import requests

main_api = "https://api.chucknorris.io/jokes/random"


print("https://api.chucknorris.io/jokes/random"+ main_api)

while True:
    try:
        user_input = input("Presiona Enter para obtener un chiste de Chuck Norris o escribe 'exit' para salir: ")
        
        if user_input.lower() == 'exit':
            print("Hasta Luego!")
            break 
        
        json_data = requests.get(main_api).json()
        
        joke = json_data['value']
        
        print("Chuck Norris broma: " + joke)
        
    except Exception as e:
        print("Ocurrió un error:", e)

