#!/usr/bin/env python3
"""Page-object model for the Create Watch List Entry Page.
"""

import sys
from ...driver import Driver
from ..abstract_page.abstract_page import AbstractPage
from selenium.webdriver.common.by import By
from .create_watch_list_entry_command import CreateWatchListEntryCommand

class CreateWatchListEntryPage(AbstractPage):
    """Page-object model for the Create Watch List Entry Page.
    """

    #The url path for the Create Watch List Entry Page.
    _path = "WatchList/Create"
    #The page name displayed on the Create Watch List Entry Page.
    _page_name = "Create Watch List Entry"

    #Selectors that selenium uses to access elements on the page are stored in this dictionary.
    _selectors = {
		'bounty' : (By.ID, 'DepartureAirport'),
		'first_name' : (By.ID, 'FirstName'),
		'last_name' : (By.ID, 'LastName'),
		'create_button' : (By.ID, 'btnCreate'),
    }

    @classmethod
    def create_entry(self):
        """This function provides a fluent API to create a watch list entry.

        Fluent API Usage:
            create_entry().with_bounty(123).with_first_name('abc').with_last_name('xyz').submit_form()

        Args:
            None
        
        Returns:
            A CreateWatchListEntryCommand object.
        """
        return CreateWatchListEntryCommand(self._selectors)

    @classmethod
    def is_at(self):
        """Determine if the browser is on the Create Watch List Entry Page.

        Args:
            None

        Returns:
            True if the browser is on the Create Watch List Entry Page.
            False if the browser is not on the Create Watch List Entry Page.
        """
        return super().is_at()

    @classmethod
    def is_at_with_exception(self):
        """Throw an exception if the browser is not on the Create Watch List Entry Page.

        Args:
            None.

        Returns:
            True if the browser is on the Create Watch List Entry Page.
            Throws an exception if the browser is not on the Create Watch List Entry Page.
        """
        return super().is_at_with_exception()

    @classmethod
    def go_to(self):
        """Navigate to the Create Watch List Entry Page.

        Args:
            None

        Returns:
            None
        """
        super().go_to(self._path)


if __name__ == '__main__':
	pass