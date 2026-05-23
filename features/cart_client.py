import requests

class CartClient:
    def __init__(self, base_url="https://fakestoreapi.com"):
        self.base_url = base_url

    def create_cart(self, cart_data: dict) -> dict:
        url = f"{self.base_url}/carts"
        response = requests.post(url, json=cart_data)
        response.raise_for_status() 
        return response