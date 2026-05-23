from behave import given, when, then
import requests

API_BASE_URL = "https://fakestoreapi.com"


@given("products are registered in the system")
def step_given_products_exist(context):
    pass


@given("a product with a valid ID exists")
def step_given_product_exists(context):
    context.product_id = 1


@when("the customer requests the product list")
def step_when_list_products(context):

    context.response = requests.get(
        f"{API_BASE_URL}/products"
    )


@when("the customer requests the product by ID")
def step_when_get_product_by_id(context):

    context.response = requests.get(
        f"{API_BASE_URL}/products/{context.product_id}"
    )


@when("the customer requests a product with a non-existing ID")
def step_when_get_nonexistent_product(context):

    context.response = requests.get(
        f"{API_BASE_URL}/products/9999"
    )


@then("the API should return a list of available products")
def step_then_list_of_products(context):

    data = context.response.json()

    assert isinstance(data, list)

    assert len(data) > 0


@then("the API should return the product details")
def step_then_product_details(context):

    data = context.response.json()

    assert "id" in data

    assert "title" in data

    assert "price" in data


