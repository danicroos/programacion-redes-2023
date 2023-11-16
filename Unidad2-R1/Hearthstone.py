'''
Descripcion: Hearthstone
Author: Zuñiga Olvera Jorge Daniel
Fecha: 16-11-2023
'''
import http.client
import json

def fetch_data():
    conn = http.client.HTTPSConnection("omgvamp-hearthstone-v1.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': 'f1bfb4a9f7msh7407a5f55245c33p17409ajsnf005dd1a9a58',
        'X-RapidAPI-Host': 'omgvamp-hearthstone-v1.p.rapidapi.com'
    }

    conn.request("GET", "/info", headers=headers)

    res = conn.getresponse()
    data = res.read()

    if res.status == 200:
        print(json.loads(data.decode("utf-8")))
    else:
        print("Error de respuesta del servidor:", data.decode("utf-8"))
        print("Código de estado:", res.status)

    conn.close()

fetch_data()
