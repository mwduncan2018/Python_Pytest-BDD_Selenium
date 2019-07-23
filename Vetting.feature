Feature: Vetting
    Passengers should be flagged if they are on the watch list.
    Passengers should not be flagged if they are not on the watch list.

    Scenario Outline: Passenger schedules flight, passenger is on the watch list
        Given DSF navigates to the Login Page
        And logging in with a valid username and password combo
        When a passenger schedules a flight <firstName> <lastName> <departureTime> <departureAiport> <arrivalTime> <arrivalAirport>
        And a passenger is added to the watch list <firstName> <lastName> <bounty>
        Then a passenger is checked on the Flights Page <firstName> <lastName>

        Examples:
        | bounty | firstName | lastName | departureTime        | departureAirport | arrivalTime          | arrivalAirport |
        | 180000 | Derek     | Chapman  | 10/1/2019 6:00:00 AM | BWI              | 10/1/2019 9:00:00 AM | NYC            |
        | 190000 | Doug      | Daniels  | 11/1/2019 9:00:00 AM | Miami            | 11/1/2019 9:00:00 AM | Chicago        |

    Scenario Outline: Passenger schedules flight, passenger is not on the watch list
        Given DSF navigates to the Login Page
        And logging in with a valid username and password combo
        When a passenger schedules a flight <firstName> <lastName> <departureTime> <departureAiport> <arrivalTime> <arrivalAirport>
        Then a passenger is not checked on the Flights Page <firstName> <lastName>

        Examples:
        | bounty | firstName | lastName | departureTime       | departureAirport | arrivalTime         | arrivalAirport |
        | 150000 | Andrew    | Ambrosia | 9/1/2019 6:00:00 AM | BWI              | 9/1/2019 9:00:00 AM | Chicago        |
        | 170000 | Mickey    | Mouse    | 8/1/2019 9:00:00 AM | NYC              | 8/1/2019 9:00:00 AM | LAX            |