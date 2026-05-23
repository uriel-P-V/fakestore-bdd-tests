API_BASE_URL = "https://fakestoreapi.com"

MOCK_CART = {
    "id": 11,
    "userId": 1,
    "date": "2026-05-22",
    "products": [{"productId": 1, "quantity": 2}]
}

VALID_CART_DATA = {
    "userId": 1,
    "date": "2026-05-22",
    "products": [{"productId": 1, "quantity": 2}]
}

def mock_cart_post(url, **kwargs):
    from unittest.mock import MagicMock
    mock = MagicMock()
    mock.status_code = 201
    mock.json.return_value = MOCK_CART
    return mock