from unittest.mock import patch, MagicMock
from features.mocks.products_mock import mock_products_get
from features.mocks.cart_mock import mock_cart_post
from features.mocks.users_mock import mock_users_get

API_BASE_URL = "https://fakestoreapi.com"

def unified_mock_get(url, **kwargs):
    if "/products" in url:
        return mock_products_get(url, **kwargs)
    elif "/users" in url:
        return mock_users_get(url, **kwargs)
    elif "/ping" in url:
        mock = MagicMock()
        mock.status_code = 200
        mock.json.return_value = {}
        return mock
    mock = MagicMock()
    mock.status_code = 200
    return mock

def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")
    if "regression" in scenario.tags:
        context.mock_get = patch("requests.get", side_effect=unified_mock_get)
        context.mock_post = patch("requests.post", side_effect=mock_cart_post)
        context.mock_get.start()
        context.mock_post.start()

def after_scenario(context, scenario):
    print(f"Finished scenario: {scenario.name} - Status: {scenario.status}")
    if "regression" in scenario.tags:
        context.mock_get.stop()
        context.mock_post.stop()