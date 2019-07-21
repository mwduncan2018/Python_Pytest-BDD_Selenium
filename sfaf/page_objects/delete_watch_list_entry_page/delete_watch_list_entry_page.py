#!/usr/bin/env python3
"""Page-object model for the Delete Watch List Entry Page.
"""

import sys
from ...driver import Driver
from ..abstract_page.abstract_page import AbstractPage
from selenium.webdriver.common.by import By

class DeleteWatchListEntryPage(AbstractPage):
    """Page-Object Model for the Delete Watch List Entry Page.
    """

    #The url path for the Delete Watch List Entry Page.
    _path = "WatchList/Delete"
    #The page name displayed on the Delete Watch List Entry Page.
    _page_name = "Delete Watch List Entry"

    #Selectors that selenium uses to access elements on the page are stored in this dictionary.
    _selectors = {
        'delete_button' : (By.ID, "btnDelete"),
    }
    
    @classmethod
    def is_at(self):
        """Determine if the browser is on the Delete Watch List Entry Page.

        Args:
            None

        Returns:
            True if the browser is on the Delete Watch List Entry Page.
            False if the browser is not on the Delete Watch List Entry Page.
        """
        super().is_at()

    @classmethod
    def is_at_with_exception(self):
        """Throw an exception if the browser is not on the Delete Watch List Entry Page.

        Args:
            None.

        Returns:
            True if the browser is on the Delete Watch List Entry Page.
            Throws an exception if the browser is not on the Delete Watch List Entry Page.
        """
        return super().is_at_with_exception()

    @classmethod
    def go_to(self):
        """Navigate to the Delete Watch List Entry Page. This will fail because an ID is not provided.

        Args:
            None

        Returns:
            None
        """
        super().go_to(self._path)

    @classmethod
    def click_delete_button(self):
        """Clicks the delete button to delete the watch list entry.

        Args:
            None
        
        Returns:
            None
        """
        self.is_at_with_exception()
        Driver.instance.find_element(*self._selectors['delete_button']).click()


if __name__ == "__main__":
    pass