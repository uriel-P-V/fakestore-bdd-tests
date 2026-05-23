API_BASE_URL = "https://fakestoreapi.com"

MOCK_USER = {
    "id": 1,
    "email": "john@gmail.com",
    "username": "johnd",
    "password": "m38rmF$",
    "name": {"firstname": "john", "lastname": "doe"},
    "address": {
        "city": "kilcoole",
        "street": "new road",
        "number": 7682,
        "zipcode": "12926-3874"
    },
    "phone": "1-570-236-7033"
}

def mock_users_get(url, **kwargs):
    from unittest.mock import MagicMock
    mock = MagicMock()
    if url == f"{API_BASE_URL}/users/1":
        mock.status_code = 200
        mock.json.return_value = MOCK_USER
    else:
        mock.status_code = 200
        mock.json.return_value = None
        mock.text = "null"
    return mock