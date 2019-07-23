#!/usr/bin/env python3
"""Page-object model for the Watch List Page.
"""

import sys
from ...driver import Driver
from ..abstract_page.abstract_page import AbstractPage
from ..delete_watch_list_entry_page.delete_watch_list_entry_page import DeleteWatchListEntryPage
from selenium.webdriver.common.by import By

class WatchListPage(AbstractPage):
    """Page-Object Model for the Watch List Page.
    """

    #The url path for the Watch List Page
    _path = "WatchList"
    #The page name displayed on the Watch List Page
    _page_name = "Watch List"

    #Selectors that selenium uses to access elements on the page are stored in this dictionary.
    _selectors = {
        'bounty_column' : (By.ID, "bounty"),
        'first_name_column' : (By.ID, "firstName"),
        'last_name_column' : (By.ID, "lastName"),
        'edit_column' : (By.LINK_TEXT, "Edit"),
        'details_column' : (By.LINK_TEXT, "Details"),
        'delete_column' : (By.LINK_TEXT, "Delete"),
        'create_watch_list_entry_button' : (By.LINK_TEXT, "Create New"),
    }

    #The data from the Watch List Page table is stored in this dictionary.
    _table = {
        'bounty_column' : None,
        'first_name_column' : None,
        'last_name_column' : None,
        'edit_column' : None,
        'details_column' : None,
        'delete_column' : None,
    }

    @classmethod
    def refresh_table(self):
        """Load the data of the Watch List table into memory.

        Args:
            None

        Returns:
            None
        """
        self._table['bounty_column'] = Driver.instance.find_elements(*self._selectors['bounty_column'])
        self._table['first_name_column'] = Driver.instance.find_elements(*self._selectors['first_name_column'])
        self._table['last_name_column'] = Driver.instance.find_elements(*self._selectors['last_name_column'])
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
    def add_to_watch_list(self, last_name, first_name, bounty):
        self.is_at_with_exception()
        #CreateWatchListEntryPage.go_to()
        pass

    @classmethod
    def delete_from_watch_list(self, last_name, first_name):
        self.is_at_with_exception()
        i = self.index_of(last_name, first_name)
        if i >= 0:
            self._table['delete_column'][i].click()
            DeleteWatchListEntryPage.click_delete_button()


if __name__ == "__main__":
    pass