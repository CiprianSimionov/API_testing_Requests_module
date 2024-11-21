import unittest

from API_testing.requests_folder.order_requests import submit_an_order, get_an_order, update_an_order, \
    delete_an_order


class TestOrders(unittest.TestCase):
    def test_get_an_order(self):
        # bookId can have values between 1 and 6 inclusively
        # and has availability (can be checked with GET list of books request)
        submit_order_response = submit_an_order(5, "Ciprian15")
        # print(submit_order_response.json())
        order_id = submit_order_response.json()["orderId"]
        # print(order_id)
        get_order_response = get_an_order(order_id)
        assert get_order_response.status_code == 200
        assert get_order_response.json()["bookId"] == 5
        assert get_order_response.json()["customerName"] == "Ciprian15"

    def test_update_an_order(self):
        submit_order_response = submit_an_order(3, "Ciprian20")
        order_id = submit_order_response.json()["orderId"]
        update_an_order_response = update_an_order(order_id)
        assert update_an_order_response.status_code == 204

    def test_submit_an_order(self):
        submit_order_response = submit_an_order(4, "Ciprian18")
        assert submit_order_response.status_code == 201
        assert submit_order_response.json()["created"] == True

    def test_delete_an_order(self):
        submit_an_order_response = submit_an_order(5, "client")
        order_id = submit_an_order_response.json()["orderId"]
        delete_an_order_response = delete_an_order(order_id)
        assert delete_an_order_response.status_code == 204

    def test_post_an_order_with_unavailable_book(self):
        submit_an_order_response = submit_an_order(2, "test invalid")
        assert submit_an_order_response.status_code == 404
        assert submit_an_order_response.json()["error"] == "This book is not in stock. Try again later."

    def test_delete_an_order_with_unavailable_orderid(self):
        submit_an_order_response = submit_an_order(1, "default Client")
        order_id = submit_an_order_response.json()["orderId"]
        delete_an_order(order_id)
        #becomes unavailable when orderId is already deleted
        delete_an_order_response = delete_an_order(order_id)
        assert delete_an_order_response.status_code == 404
        assert delete_an_order_response.json()["error"] == f"No order with id {order_id}."


