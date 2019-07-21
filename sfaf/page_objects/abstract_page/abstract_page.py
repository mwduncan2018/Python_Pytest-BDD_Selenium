#!/usr/bin/env python3
"""Page-object model for the abstract page that holds common functionality of all pages.
"""

import sys
from ...driver import Driver
from selenium.webdriver.common.by import By

class AbstractPage:
    """Page-Object Model for the abstract page.
    """

    #Selectors that selenium uses to access elements are stored in this dictionary.
    _abstract_page_selectors = {
        'actual_page_name' :  (By.ID, "pageName"),
    }

    #Part of the URL for the website.
    _url = r'http://localhost:60030/'
    #The page name.
    _page_name = None

    @classmethod
    def is_at(self):
        """Determine if the browser is currently on the expected page.

        Args:
            None
        
        Returns:
            True if the browser is on the expected page.
            False if the browser is not on the expected page.
        """
        actual_page_name = Driver.instance.find_element(*self._abstract_page_selectors['actual_page_name']).text
        if actual_page_name == self._page_name:
            return True
        else:
            return False

    @classmethod
    def is_at_with_exception(self):
        """Throw an exception if the browser is not on the expected page.

        Args:
            None
        
        Returns:
            True if the browser is on the expected page.
            Throws an exception if the browser is not on the expected page.
        """
        if self.is_at() == False:
            raise Exception("EXCEPTION! NOT ON CORRECT PAGE -- EXPECTED (" + self._page_name + ") -- ACTUAL (" + actual_page_name + ")")
        else:
            return True

    @classmethod
    def go_to(self, path):
        """Navigate to the page.

        Args:
            None
        
        Returns:
            None
        """
        Driver.instance.get(self._url + path)


if __name__ == '__main__':
	pass