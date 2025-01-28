import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'f6b71d99fb8c7736353e3c2c6d18e81d'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '18114'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_name'] == 'Леонора'