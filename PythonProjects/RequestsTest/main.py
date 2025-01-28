import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f6b71d99fb8c7736353e3c2c6d18e81d'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}

body_creation = {
    "name": "Лёня",
    "photo_id": 800
}

body_change = {
    "pokemon_id": "205670",
    "name": "Леон",
    "photo_id": 800
}

body_pokeball = {
    "pokemon_id": "205670"
}

response_creation = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creation)
print(response_creation.text)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)