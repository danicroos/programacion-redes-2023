'''
Descripcion: 
Author: Zuñiga Olvera Jorge Daniel
Fecha: 29-11-2023
'''
import requests

def hacer_consulta():
    url = 'https://free-nba.p.rapidapi.com/players'
    params = {'page': '0', 'per_page': '25'}
    headers = {
        'X-RapidAPI-Key': 'f1bfb4a9f7msh7407a5f55245c33p17409ajsnf005dd1a9a58',
        'X-RapidAPI-Host': 'free-nba.p.rapidapi.com'
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    return response.json()

def main():
    respuestas = []

    try:
        while True:
            data = hacer_consulta()
            respuestas.append(data)
            print(data)

            respuesta = input("¿Quieres consultar otra vez? (s/n): ")
            if respuesta.lower() != 's':
                break

        print("Lista de respuestas:")
        for i, respuesta in enumerate(respuestas, start=1):
            print(f"Consulta {i}: {respuesta}")

    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()

