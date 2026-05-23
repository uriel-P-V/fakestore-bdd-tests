API_BASE_URL = "https://fakestoreapi.com"

MOCK_PRODUCT = {
    "id": 1,
    "title": "Test Backpack",
    "price": 109.95,
    "category": "men's clothing",
    "rating": {"rate": 3.9, "count": 120}
}

MOCK_PRODUCT_LIST = [MOCK_PRODUCT]

def mock_products_get(url, **kwargs):
    from unittest.mock import MagicMock
    mock = MagicMock()
    if url == f"{API_BASE_URL}/products":
        mock.status_code = 200
        mock.json.return_value = MOCK_PRODUCT_LIST
    elif url == f"{API_BASE_URL}/products/1":
        mock.status_code = 200
        mock.json.return_value = MOCK_PRODUCT
    else:
        # producto no existente — igual que la API real
        mock.status_code = 200
        mock.text = ""
        mock.json.side_effect = Exception("No JSON")
    return mock