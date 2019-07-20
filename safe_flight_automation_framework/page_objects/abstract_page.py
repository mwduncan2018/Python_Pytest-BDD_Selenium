#!/usr/bin/env python3
"""Page-object model for the abstract page that holds common functionality of all pages.
"""

import sys
from ..driver import Driver
from selenium.webdriver.common.by import By

class AbstractPage:
    _PAGE_NAME = (By.ID, "pageName")

    _page_name = None
    _url = r'http://localhost:60030/'

    @classmethod
    def is_at(self):
        actual_page_name = Driver.instance.find_element(self._PAGE_NAME).get_text()
        if actual_page_name is self._page_name:
            return True
        else:
            raise Exception("EXCEPTION! NOT ON CORRECT PAGE -- EXPECTED ({}) -- ACTUAL ({})".format([self._page_name, actual_page_name]))

    @classmethod
    def go_to(self, path):
        Driver.instance.get(self._url + path)

if __name__ == '__main__':
	print("Executing main")
	pass