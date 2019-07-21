#!/usr/bin/env python3
"""The Driver for Selenium.
"""

import os, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen

class Driver:
    """The instance of the Driver is a singleton.
    """

    #This is the single global instance of the Driver
    instance = None
    #Chromedriver executable path
    _chromedriver_executable_path = r"C:\dev\Webdrivers\chromedriver.exe"

    @classmethod
    def shutdown(self):
        """Shutdown the Driver and set the instance to None.

        Args:
            None

        Returns:
            None
        """
        self.instance.close()
        self.instance = None

    @classmethod
    def initialize(self):
        """Startup the Driver.

        Args:
            None

        Returns:
            None
        """
        if self.instance is None:
            options = Options()
            options.add_argument("--start-maximized")
            self.instance = webdriver.Chrome(executable_path=self._chromedriver_executable_path, chrome_options=options)
            self.instance.implicitly_wait(5)

    @classmethod
    def init(self):
        """Shorthand for initialize()
        """
        self.initialize()


if __name__ == '__main__':
	pass	