#!/usr/bin/env python3
"""CreateWatchListEntryCommand provides a fluent API for the Create Watch List Page.
"""

import sys
from ...driver import Driver
from selenium.webdriver.common.by import By

class CreateWatchListEntryCommand:
    def __init__(self, selectors):
        self._bounty = ""
        self._first_name = ""
        self._last_name = ""
        self._selectors = selectors
    def with_bounty(self, bounty):
        self._bounty = str(bounty)
        return self
    def with_first_name(self, first_name):
        self._first_name = first_name
        return self
    def with_last_name(self, last_name):
        self._last_name = last_name
        return self
    def submit_form(self):
        Driver.instance.find_element(*self._selectors['bounty']).send_keys(self._bounty)
        Driver.instance.find_element(*self._selectors['first_name']).send_keys(self._first_name)
        Driver.instance.find_element(*self._selectors['last_name']).send_keys(self._last_name)
        Driver.instance.find_element(*self._selectors['create_button']).click()

        
if __name__ == '__main__':
    pass