import requests
from faker import Faker


def generate_token(name="", email=""):
    faker_object = Faker()
    if name == "" and email != "":
        name = faker_object.name()
    elif name != "" and email == "":
        email = faker_object.email()
    elif name == "" and email == "":
        name = faker_object.name()
        email = faker_object.email()
    else:
        name = name
        email = email
    faker_data = {
        "clientName": name,
        "clientEmail": email
    }
    response = requests.post("https://simple-books-api.glitch.me/api-clients/", json=faker_data)
    return response.json()["accessToken"]
