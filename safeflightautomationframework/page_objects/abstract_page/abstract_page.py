#!/usr/bin/env python3
"""Page-object model for the abstract page that holds common functionality of all pages."""

import sys, os
from ...driver import Driver
from selenium.webdriver.common.by import By


class AbstractPage:
    """Page-Object Model for the abstract page."""

    # Selectors that selenium uses to access elements are stored in this dictionary.
    _abstract_page_selectors = {
        'actual_page_name': (By.ID, "pageName"),
        'logout_link': (By.LINK_TEXT, "Logout"),
    }

    # Part of the URL for the website.
    _url = r'http://localhost:60030/'
    _path = ""
    # The page name.
    _page_name = None

    @classmethod
    def is_at(cls):
        """Determine if the browser is currently on the expected page.
        Returns:
            True if the browser is on the expected page.
            False if the browser is not on the expected page.
        """
        actual_page_name = Driver.instance.find_element(*cls._abstract_page_selectors['actual_page_name']).text
        if actual_page_name == cls._page_name:
            return True
        else:
            return False

    @classmethod
    def is_at_with_exception(cls):
        """Throw an exception if the browser is not on the expected page.
        Returns:
            True if the browser is on the expected page.
            Throws an exception if the browser is not on the expected page.
        """
        actual_page_name = Driver.instance.find_element(*cls._abstract_page_selectors['actual_page_name']).text
        if actual_page_name == cls._page_name:
            return True
        else:
            raise Exception(
                "NOT ON EXPECTED PAGE! --> EXPECTED (" + cls._page_name + ") --> ACTUAL (" + actual_page_name + ")")

    @classmethod
    def go_to(cls):
        """Navigate to the page."""
        Driver.instance.get(cls._url + cls._path)

    @classmethod
    def logout_is_displayed(cls):
        """Determine if the link to 'Logout' is displayed.
        Returns:
            True if the 'Logout' link is displayed.
            False if the 'Logout' link is not displayed.
        """
        try:
            Driver.instance.find_element(*cls._abstract_page_selectors['logout_link'])
            return True
        except:
            return False


if __name__ == '__main__':
    pass
