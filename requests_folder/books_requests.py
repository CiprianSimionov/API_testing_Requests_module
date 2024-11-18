import requests


def get_list_of_books():
    response = requests.get("https://simple-books-api.glitch.me/books")
    return response


def get_list_of_books_with_parameters(book_type, book_limit):
    response = requests.get(f"https://simple-books-api.glitch.me/books?type={book_type}&limit={book_limit}")
    return response
