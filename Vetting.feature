Feature: Vetting
    Passengers should be flagged if they are on the watch list.
    Passengers should not be flagged if they are not on the watch list.

    Scenario: Passenger schedules flight, passenger is on the watch list
        Given DSF navigates to the Login Page
        And logging in with a valid username and password combo
        When a regular passenger schedules a flight
        Then a passenger is checked on the Flights Page
        And clean up regular passenger data

    Scenario: Passenger schedules flight, passenger is not on the watch list
        Given DSF navigates to the Login Page
        And logging in with a valid username and password combo
        When a watched passenger schedules a flight
        And a passenger is added to the watch list
        Then a passenger is not checked on the Flights Page
        And clean up watched passenger data