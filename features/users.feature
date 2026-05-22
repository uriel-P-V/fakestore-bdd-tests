Feature: Users API  

    Background:
        Given the Store API is available
    @smoke
    Scenario: Get user by valid userId
        When I request the user with ID 1
        Then the response status code should be 200
        And the response should contain user information

    @regression
    Scenario: Validate user response fields
        When I request the user with ID 1
        Then the response status code should be 200
        And the response should contain the user fields:
            | id |
            | email |
            | username |
            | password |
            | name |
            | address | 
            | phone |

    @regression
    Scenario: Get user with invalid userId
        When I request the user with ID 999999
        Then the response status code should be 200
        And the response body should be empty