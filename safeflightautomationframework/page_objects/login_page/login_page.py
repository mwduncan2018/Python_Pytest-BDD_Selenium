#!/usr/bin/env python3
"""Page-object model for the Login Page.
"""

import sys
from ...driver import Driver
from ..abstract_page.abstract_page import AbstractPage
from selenium.webdriver.common.by import By
from .login_command import LoginCommand

class LoginPage(AbstractPage):
    """Page-Object Model for the Login Page.
    """

    #The url path for the Login Page.
    _path = "Login"
    #The page name displayed on the Login Page.
    _page_name = "Login"

    #Selectors that selenium uses to access elements on the page are stored in this dictionary.
    _selectors = {
        'username' : (By.ID, "Username"),
        'password' : (By.ID, "Password"),
        'login_button' : (By.ID, "btnLogin"),
        'username_validation' : (By.ID, "Username-error"),
        'password_validation' : (By.ID, "Password-error"),
        'validation_summary' : (By.ID, "viewBagValidationSummary"),
    }

    @classmethod
    def login_as(self, username):
        """Login with this fluent API.

        Fluent-API Usage:
            login_as('username').with_password('password').submit_form()

        Args:
            username: The username to login with.
        
        Returns:
            A LoginCommand object is returned.
        """
        return LoginCommand(username, self._selectors)

    @classmethod
    def username_validation_is_displayed(self):
        """Determine if the text of the username validation is displayed properly.

        Args:
            None

        Returns:
            True if text of the username validation is correctly displayed.
            False if text of the username validation is not correctly displayed.
        """
        self.is_at()
        return Driver.instance.find_element(*self._selectors['username_validation']).text == "The Username field is required."
    
    @classmethod
    def password_validation_is_displayed(self):
        """Determine if the text of the password validation is displayed properly.

        Args:
            None

        Returns:
            True if text of the username password is correctly displayed.
            False if text of the username password is not correctly displayed.
        """
        self.is_at()
        return Driver.instance.find_element(*self._selectors['password_validation']).text == "The Password field is required."
    
    @classmethod
    def validation_username_password_combination_invalid(self):
        """Determine if the validation message for an invalid username/password combination dispalys correctly.

        Args:
            None

        Returns:
            True if text of the validation displays correctly.
            False if text of the validation does not display correctly.
        """
        self.is_at()
        return Driver.instance.find_element(*self._selectors['validation_summary']).text == "The username/password combination is invalid."


if __name__ == "__main__":
    pass