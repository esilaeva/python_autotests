import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
TOKEN = 'your_token'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN 
}


#  - Проверь, что ответ запрос **GET /trainers** приходит с кодом 200    
def test_get_trainers():
    """
    KTI-1. Get trainers. Status code 200
    """
    response = requests.get(url=f'{URL}/trainers', timeout=3)
    assert response.status_code == 200, 'Unexpected status code'


# - Проверь, что в ответе приходит строчка с именем твоего тренера
def test_get_trainer_by_id():
    """
    KTI-2. Get trainer by id 
    """
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id':3550}, timeout=3)
    assert response.json()['trainer_name'] == 'Elena', ''