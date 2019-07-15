#!/usr/bin/env python3
"""Driver for Selenium.

Usage:

	python3 driver.py
"""

import os
import sys
from selenium import webdriver
from urllib.request import urlopen

class Driver:
    instance = None

    @classmethod
    def initialize(cls):
        os.environ['webdriver.gecko.driver'] = r'C:\Users\mwdun\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe'
        if cls.instance is None:
            cls.instance = webdriver.Firefox()
            cls.instance.implicitly_wait(15)

    @classmethod
    def close(cls):
        cls.instance.close()


if __name__ == '__main__':
	print("Executing main")
	pass	