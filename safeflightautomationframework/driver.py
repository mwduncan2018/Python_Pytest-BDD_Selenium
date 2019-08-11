#!/usr/bin/env python3
"""The Driver for Selenium."""

import os, sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen

class Driver:
    """The instance of the Driver is a singleton."""

    instance = None
    _chrome_driver_executable_path = r"C:\dev\Webdrivers\chromedriver.exe"

    @classmethod
    def shutdown(cls):
        """Shutdown the Driver and set the instance to None."""
        cls.instance.close()
        cls.instance = None

    @classmethod
    def initialize(cls):
        """Startup the Driver."""
        if cls.instance is None:
            options = Options()
            options.add_argument("--start-maximized")
            cls.instance = webdriver.Chrome(executable_path=cls._chrome_driver_executable_path, chrome_options=options)
            cls.instance.implicitly_wait(5)

    @classmethod
    def init(cls):
        """Shorthand for initialize()"""
        cls.initialize()

    @classmethod
    def get_page_source(cls):
        return cls.instance.page_source

if __name__ == '__main__':
    pass
