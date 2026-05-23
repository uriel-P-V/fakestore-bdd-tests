from behave import given, then
import requests

API_BASE_URL = "https://fakestoreapi.com"

@given("the Store API is available")
def step_given_api_available(context):
    context.response = requests.get(f"{API_BASE_URL}/products")
    assert context.response.status_code == 200


@then("the response status code should be {expected_status:d}")
def step_then_status_code(context, expected_status):
    assert context.response.status_code == expected_status


@then("the response body should be empty")
def step_then_empty_body(context):
    text = context.response.text.strip()
    if text == "" or text == "null":
        return  # ambos son válidos como "vacío"
    try:
        data = context.response.json()
        assert data is None, f"Expected empty body but got: {data}"
    except requests.exceptions.JSONDecodeError:
        assert text == "", f"Expected empty body but got: {text}"