#!/usr/bin/env python3
"""Page-object model for the Create Flight Page.
"""

import sys
from ...driver import Driver
from ..abstract_page.abstract_page import AbstractPage
from selenium.webdriver.common.by import By
from .create_flight_command import CreateFlightCommand

class CreateFlightPage(AbstractPage):
    """Page-Object Model for the Create Flight Page.
    """

    #The url path for the Create Flight Page.
    _path = "Flights/Create"
    #The page name displayed on the Create Flight Page.
    _page_name = "Create Flight"

    #Selectors that selenium uses to access elements on the page are stored in this dictionary.
    _selectors = {
		'departure_airport' : (By.ID, 'DepartureAirport'),
		'arrival_airport' : (By.ID, 'ArrivalAirport'),
		'departure_time' : (By.ID, 'DepartureTime'),
		'arrival_time' : (By.ID, 'ArrivalTime'),
		'first_name' : (By.ID, 'FirstName'),
		'last_name' : (By.ID, 'LastName'),
		'create_button' : (By.ID, 'btnCreate'),
    }

    @classmethod
    def create_flight(self):
        """This function exposes a fluent API to Create a Flight.

        Fluent-API Usage:
            create_flight().with_departure_airport('xyz').with_arrival_airport('xyz').with_departure_time('xyz')
				.with_arrival_time('xyz').with_first_name('xyz').with_password('xyz').submit_form()

        Args:
            None
        
        Returns:
            This function returns a CreateFlightCommand object.
        """
        return CreateFlightCommand(self._selectors)

    @classmethod
    def is_at(self):
        """Determine if the browser is on the Create Flight Page.

        Args:
            None

        Returns:
            True if the browser is on the Create Flight Page.
            False if the browser is not on the Create Flight Page.
        """
        return super().is_at()

    @classmethod
    def is_at_with_exception(self):
        """Throw an exception if the browser is not on the Create Flight Page.

        Args:
            None.

        Returns:
            True if the browser is on the Create Flight Page.
            Throws an exception if the browser is not on the Create Flight Page.
        """
        return super().is_at_with_exception()

    @classmethod
    def go_to(self):
        """Navigate to the Create Flight Page.

        Args:
            None

        Returns:
            None
        """
        super().go_to(self._path)


if __name__ == '__main__':
	pass