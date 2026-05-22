Feature: Cart API

    Background:
        Given the Store API is available
    @smoke
    Scenario: Create a cart successfully
        When I create a cart with valid products
        Then the response status code should be 201
        And the response should contain the created cart information

    @regression
    Scenario: Validate the cart response structure
        When I create a cart with valid products
        Then the response status code should be 201
        And the response should contain the cart fields:
            | id |
            | userId |
            | date |
            | products |
    
    @regression
    Scenario: Create cart request timeout
        When I create a cart but the request times out
        Then the request should fail with a timeout error