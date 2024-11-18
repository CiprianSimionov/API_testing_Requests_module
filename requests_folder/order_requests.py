import requests

from API_testing.requests_folder.generate_token_request import generate_token


token = generate_token()


def submit_an_order(book_id, customer_name):
    header = {'Authorization': token}
    data = {
        "bookId": book_id,
        "customerName": customer_name
    }
    response = requests.post("https://simple-books-api.glitch.me/orders", headers=header, json=data)
    return response


def update_an_order(order_id):
    header = {'Authorization': token}
    data = {
        "customerName": "Markus"
    }
    response = requests.patch(f"https://simple-books-api.glitch.me/orders/{order_id}", headers=header, json=data)
    return response


def get_an_order(order_id):
    header = {'Authorization': token}
    response = requests.get(f"https://simple-books-api.glitch.me/orders/{order_id}", headers=header)
    return response


def delete_an_order(order_id):
    header = {'Authorization': token}
    response = requests.delete(f"https://simple-books-api.glitch.me/orders/{order_id}", headers=header)
    return response
