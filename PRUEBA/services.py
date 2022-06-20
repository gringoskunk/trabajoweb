import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_pokemon():
    json_response = generate_request('http://localhost:8000/pokemonapi')

    if json_response:
       pokemon = json_response['results'][0]
       print (pokemon)
       return pokemon
    return { 'error': 'No se pudo obtener el pokemon' }