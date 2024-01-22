import requests

URL = 'https://api.pokemonbattle.me:9104'
TOKEN = 'your_token'
HEADER = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN 
}

# - Создание покемона (**POST /pokemons** (*не забудь про нужный хэдер*))
# В ответе (терминале) должен прийти объект json
body = {
    "name": "NewPok",
    "photo": "https://dolnikov.ru/pokemons/albums/218.png"
}
response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER)
print(f'Status code: {response.status_code}. Message: {response.json()["message"]}')


# # - Смена имени покемона (**PUT /pokemons** (*не забудь про нужный хэдер*))
# # В ответе (терминале) должен прийти объект json
body = {
    "pokemon_id": "28320",
    "name": "OldPok",
    "photo": "https://dolnikov.ru/pokemons/albums/055.png"
}
response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER)
print(f'Status code: {response.status_code}. Message: {response.json()["message"]}')


# - Поймать покемона в покебол (**POST /trainers/add_pokeball** (*не забудь про нужный хэдер*))
body = {
    "pokemon_id": "28320"
}
response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER)
print(f'Status code: {response.status_code}. Message: {response.json()["message"]}')