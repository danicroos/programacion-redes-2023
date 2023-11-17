'''
Descripcion: Hearthstone
Author: Zuñiga Olvera Jorge Daniel
Fecha: 16-11-2023p
'''
import http.client
import json

def fetch_data():
    conn = http.client.HTTPSConnection("omgvamp-hearthstone-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': 'f1bfb4a9f7msh7407a5f55245c33p17409ajsnf005dd1a9a58',
        'X-RapidAPI-Host': 'omgvamp-hearthstone-v1.p.rapidapi.com'
    }
    user_input = input("Escribe el endpoint de la API (por ejemplo, '/info', '/cards', etc.): ")

    api_path = f'/{user_input.strip()}'
    
    conn.request("GET", api_path, headers=headers)

    res = conn.getresponse()
    data = res.read()

    if res.status == 200:

        print(f'URL de la API: {conn.host}{api_path}')

        print(json.loads(data.decode("utf-8")))
    else:
        print("Error de respuesta del servidor:", data.decode("utf-8"))
        print("Código de estado:", res.status)

    conn.close()
fetch_data()

