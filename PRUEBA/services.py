import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_pokemon():
    response = generate_request('http://localhost:5000/pokemon')
    if response:
       pokemon = response.get()
       return pokemon
    return ''