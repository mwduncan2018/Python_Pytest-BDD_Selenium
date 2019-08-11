#!/usr/bin/env python3
"""LoginCommand is used by LoginPage to make a fluent API for the login form.
"""

import sys
from ...driver import Driver
from selenium.webdriver.common.by import By

class LoginCommand:
    def __init__(self, username, selectors):
        self._username = username
        self._password = ""
        self._selectors = selectors
    def with_password(self, password):
        self._password = password
        return self
    def submit_form(self):
        Driver.instance.find_element(*self._selectors['username']).send_keys(self._username)
        Driver.instance.find_element(*self._selectors['password']).send_keys(self._password)
        Driver.instance.find_element(*self._selectors['login_button']).click()


if __name__ == "__main__":
    pass