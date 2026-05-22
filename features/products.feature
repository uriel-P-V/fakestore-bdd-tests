Feature: Products API

    Background:
        Given the Store API is available
    @smoke
    Scenario: List available products
        Given products are registered in the system
        When the customer requests the product list
        Then the API should return a list of available products
        And the response status code should be 200

    @regression
    Scenario: Get product by valid ID
        Given a product with a valid ID exists
        When the customer requests the product by ID
        Then the API should return the product details
        And the response status code should be 200

    @regression
    Scenario: Get product by non-existing ID
        Given products are registered in the system
        When the customer requests a product with a non-existing ID
        Then the API should return an error message
        And the response status code should be 404