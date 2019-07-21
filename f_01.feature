Feature: f_01
    This is a test to get going with pytest bdd.

    Background:
        Given the webdriver is initialized

    Scenario: Login with a valid username and password
        Given DSF navigates to the Login Page
        When logging in with a valid username and password combo
        Then DSF is at the Flights Page
        And DSF is not at the Login Page

    Scenario Outline: Login with a valid username and password Parametrized
        Given DSF navigates to the Login Page
        When logging in as username <username> and password <password>
        Then DSF is at the Flights Page

        Examples:
        | username | password  |
        | tduncan  | airforce1 |
        | sharford | michigan  |
        | gduncan  | mommom    |