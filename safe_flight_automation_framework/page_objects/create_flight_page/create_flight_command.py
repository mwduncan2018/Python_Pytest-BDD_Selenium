#!/usr/bin/env python3
"""CreateFlightCommand provides a fluent API for the Create Flight Page.
"""

import sys
from ...driver import Driver
from selenium.webdriver.common.by import By

class CreateFlightCommand:
    def __init__(self, selectors):
        self._departure_airport = ""
        self._arrival_airport = ""
        self._departure_time = ""
        self._arrival_time = ""
        self._first_name = ""
        self._last_name = ""
        self._selectors = selectors
    def with_departure_airport(self, departure_airport):
        self._departure_airport = departure_airport
        return self
    def with_arrival_airport(self, arrival_airport):
        self._arrival_airport = arrival_airport
        return self
    def with_departure_time(self, departure_time):
        self._departure_time = departure_time
        return self
    def with_arrival_time(self, arrival_time):
        self._arrival_time = arrival_time
        return self
    def with_first_name(self, first_name):
        self._first_name = first_name
        return self
    def with_last_name(self, last_name):
        self._last_name = last_name
        return self
    def submit_form(self):
        Driver.instance.find_element(*self._selectors['departure_airport']).send_keys(self._departure_airport)
        Driver.instance.find_element(*self._selectors['arrival_airport']).send_keys(self._arrival_airport)
        Driver.instance.find_element(*self._selectors['departure_time']).send_keys(self._departure_time)
        Driver.instance.find_element(*self._selectors['arrival_time']).send_keys(self._arrival_time)
        Driver.instance.find_element(*self._selectors['first_name']).send_keys(self._first_name)
        Driver.instance.find_element(*self._selectors['last_name']).send_keys(self._last_name)
        Driver.instance.find_element(*self._selectors['create_button']).click()

        
if __name__ == '__main__':
    pass