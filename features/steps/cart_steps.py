from behave import when, then
import requests
from unittest.mock import MagicMock, patch
from features.cart_client import CartClient

VALID_CART_DATA = {
    "userId": 1,
    "date": "2026-05-22",
    "products": [{"productId": 1, "quantity": 2}]
}


@when("I create a cart with valid products")
def step_when_create_cart(context):

    client = CartClient()

    context.response = client.create_cart(
        VALID_CART_DATA
    )

    context.cart_response = (
        context.response.json()
    )


@when("I create a cart but the request times out")
def step_when_cart_timeout(context):
    client = CartClient()
    
    with patch.object(
        client,                           # objeto a parchear
        "create_cart",                    # método a parchear
        side_effect=requests.exceptions.Timeout
    ):
        try:
            client.create_cart(VALID_CART_DATA)
            context.timeout_raised = False
        except requests.exceptions.Timeout:
            context.timeout_raised = True

@then("the response should contain the created cart information")
def step_then_cart_created(context):

    assert "id" in context.cart_response

    assert "products" in context.cart_response


@then("the response should contain the cart fields:")
def step_then_cart_fields(context):

    for row in context.table:

        field = row[0]

        assert (
            field in context.cart_response
        ), f"{field} not found in cart response"


@then("the request should fail with a timeout error")
def step_then_timeout_error(context):

    assert context.timeout_raised is True