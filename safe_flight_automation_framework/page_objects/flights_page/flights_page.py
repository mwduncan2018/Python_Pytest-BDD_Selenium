#!/usr/bin/env python3
"""Page-object model for the Flights Page.
"""

import sys
from ...driver import Driver
from ..abstract_page.abstract_page import AbstractPage
from ..delete_flight_page.delete_flight_page import DeleteFlightPage
from selenium.webdriver.common.by import By

class FlightsPage(AbstractPage):
    """Page-Object Model for the Flights Page.
    """

    #The url path for the Flights Page
    _path = "Flights"
    #The page name displayed on the Flights Page
    _page_name = "Flight List"

    #Selectors that selenium uses to access elements on the page are stored in this dictionary.
    _selectors = {
        'watch_list_column' : (By.CSS_SELECTOR, "#watchList > input"),
        'first_name_column' : (By.ID, "firstName"),
        'last_name_column' : (By.ID, "lastName"),
        'departure_airport_column' : (By.ID, "departureAirport"),
        'departure_time_column' : (By.ID, "departureTime"),
        'arrival_airport_column' : (By.ID, "arrivalAirport"),
        'arrival_time_column' : (By.ID, "arrivalTime"),
        'edit_column' : (By.LINK_TEXT, "Edit"),
        'details_column' : (By.LINK_TEXT, "Details"),
        'delete_column' : (By.LINK_TEXT, "Delete"),
        'create_flight_button' : (By.LINK_TEXT, "Create New"),
    }

    #The data from the Flights Page table is stored in this dictionary.
    _table = {
        'watch_list_column' : None,
        'first_name_column' : None,
        'last_name_column' : None,
        'departure_airport_column' : None,
        'departure_time_column' : None,
        'arrival_airport_column' : None,
        'arrival_time_column' : None,
        'edit_column' : None,
        'details_column' : None,
        'delete_column' : None,
    }

    @classmethod
    def refresh_table(self):
        """Load the data of theFlights Page table into memory.

        Args:
            None

        Returns:
            None
        """
        self._table['watch_list_column'] = Driver.instance.find_elements(*self._selectors['watch_list_column'])
        self._table['first_name_column'] = Driver.instance.find_elements(*self._selectors['first_name_column'])
        self._table['last_name_column'] = Driver.instance.find_elements(*self._selectors['last_name_column'])
        self._table['departure_airport_column'] = Driver.instance.find_elements(*self._selectors['departure_airport_column'])
        self._table['departure_time_column'] = Driver.instance.find_elements(*self._selectors['departure_time_column'])
        self._table['arrival_airport_column'] = Driver.instance.find_elements(*self._selectors['arrival_airport_column'])
        self._table['arrival_time_column'] = Driver.instance.find_elements(*self._selectors['arrival_time_column'])
        self._table['edit_column'] = Driver.instance.find_elements(*self._selectors['edit_column'])
        self._table['details_column'] = Driver.instance.find_elements(*self._selectors['details_column'])
        self._table['delete_column'] = Driver.instance.find_elements(*self._selectors['delete_column'])

    @classmethod
    def index_of(self, last_name, first_name):
        """Determine the row index for a person in the table.
        The search is based on a match with the first name and last name.
        The search is case-sensitive.
        The search starts at index 0 and goes until the first instance of a match is found.
        -1 is returned if the person is not found.

        Args:
            last_name: The last name of the person to search for.
            first_name: The first name of the person to search for.

        Returns:
            The index of the row where a person appears in the table.
        """
        self.is_at_with_exception()
        self.refresh_table()
        i = 0
        for item in self._table['first_name_column']:
            if item.text == first_name:
                if self._table['last_name_column'][i].text == last_name:
                    return i
            else:
                i = i + 1
        return -1

    @classmethod
    def watch_list_is_checked_for(self, last_name, first_name):
        """Determine if the watch list column is checked for a person.

        Args:
            last_name: The last name of the person to search for.
            first_name: The first name of the person to search for.

        Returns:
            True if the watch list column is checked for the person.
            False if the watch list column is not checked for the person.
        """
        self.is_at_with_exception()
        i = self.index_of(last_name, first_name)
        if i >= 0:
            if self._table['watch_list_column'][i].is_selected():
                return True
            else:
                return False

    @classmethod
    def click_link_create_flight(self):
        """Click the link to create a new flight.

        Args:
            None

        Returns:
            None
        """
        self.is_at_with_exception()
        Driver.instance.find_element(*self._selectors['create_flight_button']).click()

    @classmethod
    def delete_flight(self, last_name, first_name):
        self.is_at_with_exception()
        i = self.index_of(last_name, first_name)
        if i >= 0:
            self._table['delete_column'][i].click()
            DeleteFlightPage.click_delete_button()

    @classmethod
    def flight_is_displayed(self, last_name, first_name, departure_airport, departure_time, arrival_airport, arrival_time):
        """Determine if a particular flight is displayed on the table of the Flights page.

        Args:
            last_name: The last name of the person for the flight.
            first_name: The first name of the person for the flight.
            departure_airport: The departure airport for the flight.
            departure_time: The departure time for the flight.
            arrival_airport: The arrival airport for the flight.
            arrival_time: The arrival time for the flight.

        Returns:
            True if the flight is found in the table.
            False if the flight is not found in the table.
        """
        self.is_at_with_exception()
        i = self.index_of(last_name, first_name)
        if i >= 0:
            if all([self._table['last_name_column'][i].text == last_name, self._table['first_name_column'][i].text == first_name, self._table['departure_airport_column'][i].text == departure_airport, self._table['departure_time_column'][i].text == departure_time, self._table['arrival_airport_column'][i].text == arrival_airport, self._table['arrival_time_column'][i].text == arrival_time,]):
                return True
            else:
                pass
        else:
            return False


if __name__ == "__main__":
    pass