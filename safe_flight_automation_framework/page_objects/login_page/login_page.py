#!/usr/bin/env python3
"""Page-object model for the login page.
"""

import sys
from ...driver import Driver
from ..abstract_page import AbstractPage
from selenium.webdriver.common.by import By
from .login_command import LoginCommand

class LoginPage(AbstractPage):
    _USERNAME = (By.ID, "Username")
    _PASSWORD = (By.ID, "Password")
    _LOGIN_BUTTON = (By.ID, "btnLogin")
    _USERNAME_VALIDATION = (By.ID, "Username-error")
    _PASSWORD_VALIDATION = (By.ID, "Password-error")
    _VALIDATION_SUMMARY = (By.ID, "viewBagValidationSummary")

    _path = "Login"
    _page_name = "Login"

    @classmethod
    def login_as(self, username):
        return LoginCommand(username, self._USERNAME, self._PASSWORD, self._LOGIN_BUTTON)

    @classmethod
    def is_at(self):
        super().is_at()

    @classmethod
    def go_to(self):
        super().go_to(self._path)

    @classmethod
    def username_validation_is_displayed(self):
        self.is_at()
        return Driver.instance.find_element(*_USERNAME_VALIDATION).get_text() is "The Username field is required."
    
    @classmethod
    def password_validation_is_displayed(self):
        self.is_at()
        return Driver.instance.find_element(*_PASSWORD_VALIDATION).get_text() is "The Password field is required."
    
    @classmethod
    def validation_username_password_combination_invalid(self):
        self.is_at()
        return Driver.instance.find_element(*_VALIDATION_SUMMARY).get_text() is "The username/password combination is invalid."


if __name__ == "__main__":
    pass