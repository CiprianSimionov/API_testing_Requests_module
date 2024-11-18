**API testing** - Created with python library requests for https://simple-books-api.glitch.me

* Install:
`pip install pytest`
* Run tests using:
`pytest`
* Run specific tests:
`pytest tests/test_orders.py`
* Generate html reports:
* for orders: `pytest tests/test_orders.py --html=orders_report.html`
* for books: `pytest tests/test_books.py --html=books_report.html`
* All tests: `pytest --html=full_report.html`
