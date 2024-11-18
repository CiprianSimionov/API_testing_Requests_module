from random import randint

import requests


def generate_token():
    random_nr = randint(1, 999999999)
    data = {
        "clientName": "Ciprian",
        "clientEmail": f"ciprian.simionov{random_nr}@example.com"
    }
    response = requests.post("https://simple-books-api.glitch.me/api-clients/", json=data)
    return response.json()["accessToken"]
