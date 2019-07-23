Feature: Login functionality
    This is a test to get going with pytest bdd.

    Scenario: Login, valid username, valid password
        Given DSF navigates to the Login Page
        When logging in with a valid username and password combo
        Then DSF is at the Flights Page
        And DSF is not at the Login Page

    Scenario Outline: Parametrized Login, valid username, valid password
        Given DSF navigates to the Login Page
        When logging in as username <username> and password <password>
        Then DSF is at the Flights Page

        Examples:
        | username | password  |
        | tduncan  | airforce1 |
        | sharford | michigan  |
        | gduncan  | mommom    |
    
    Scenario Outline: Parametrized Login, invalid username and password combination
        Given DSF navigates to the Login Page
        When logging in as username <username> and password <password>
        Then validation for an invalid username and password combination is displayed

        Examples:
        | username | password |
        | xyz      | xyz      |
        | tduncan  | xyz      |

    Scenario: Login, blank username, blank password
        Given DSF navigates to the Login Page
        When attempting to login with blank username and password fields
        Then validation is displayed that states the username is required
        And validation is displayed that states the password is required