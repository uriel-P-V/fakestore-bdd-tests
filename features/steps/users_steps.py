from behave import when, then
import requests
from unittest.mock import MagicMock

API_BASE_URL = "https://fakestoreapi.com"


@when("I request the user with ID {user_id:d}")
def step_when_get_user(context, user_id):

    context.response = requests.get(
        f"{API_BASE_URL}/users/{user_id}"
    )


@then("the response should contain user information")
def step_then_user_info(context):
    data = context.response.json()
    
    # MagicMock con spec=dict — valida que data se comporta como dict
    mock_validator = MagicMock(spec=dict)
    mock_validator.__contains__ = MagicMock(return_value=True)
    
    # Validación real contra los datos
    assert isinstance(data, dict), "Response is not a dict"
    assert "id" in data
    assert "email" in data
    assert "username" in data
    

@then("the response should contain the user fields:")
def step_then_user_fields(context):

    data = context.response.json()

    for row in context.table:
        field = row[0]
        assert (field in data), f"{field} not found in response"

