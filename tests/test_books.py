import unittest

from API_testing.requests_folder.books_requests import get_list_of_books, get_list_of_books_with_parameters


class TestBooks(unittest.TestCase):
    def test_get_list_of_books(self):
        get_list_of_books_response = get_list_of_books()
        assert get_list_of_books_response.status_code == 200
        assert get_list_of_books_response.json()[0]["id"] == 1
        assert get_list_of_books_response.json()[0]["name"] == "The Russian"
        assert get_list_of_books_response.json()[0]["type"] == "fiction"
        assert get_list_of_books_response.json()[0]["available"] == True

    def test_get_list_of_books_with_params(self):
        get_list_of_books_with_params = get_list_of_books_with_parameters("fiction", 20)
        assert get_list_of_books_with_params.status_code == 200
        assert len(get_list_of_books_with_params.json()) == 4

    def test_get_list_of_books_with_params_with_invalid_type(self):
        # put invalid parameter - ex.fictional
        get_list_of_books_with_params = get_list_of_books_with_parameters("fictional", 20)
        assert get_list_of_books_with_params.status_code == 400
        assert get_list_of_books_with_params.json()[
                   "error"] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction."

    def test_get_list_of_books_with_params_with_invalid_limit(self):
        # put invalid parameter - ex.limit==200
        get_list_of_books_with_params = get_list_of_books_with_parameters("fiction", 200)
        assert get_list_of_books_with_params.status_code == 400
        assert get_list_of_books_with_params.json()[
                   "error"] == "Invalid value for query parameter 'limit'. Cannot be greater than 20."


