#!/usr/bin/env python3
"""Driver for Selenium.
"""

import os
import sys
from selenium import webdriver
from urllib.request import urlopen

class Driver:
    instance = None

    @classmethod
    def shutdown(self):
        self.instance.close()
        self.instance = None

    @classmethod
    def initialize(self):
        if self.instance is None:
            self.instance = webdriver.Chrome(r"C:\dev\Webdrivers\chromedriver.exe")
            self.instance.implicitly_wait(5)
            #options = webdriver.ChromeOptions()
            #options.add_argument("--ignore-certificate-errors")
            #options.add_argument("--incognito")
            #options.add_argument("--headless")
            #self.instance = webdriver.Chrome(options=options)


if __name__ == '__main__':
	pass	