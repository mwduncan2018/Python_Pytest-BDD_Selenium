"""
Beautiful Soup
	pull data out of HTML and XML files
	simple and pythonic
	no need to worry about encodings
	multiple parsers

Python's HTML Parser
LXML
HTML5

BeautifulSoup parses into a tree of Python objects
	Tag
	NavigableString - text within a tag
	Comment - comments of the web page
	BeautifulSoup

Selenium is powerful to extract info, but it is slow
BeautifulSoup is faster

Steps:
	1) Navigate to website with Selenium
	2) Perform necessary browser actions
	3) Get page source info
	4) Pass page source to BeautifulSoup for parsing!
"""

from bs4 import BeautifulSoup
import pytest
from .safeflightautomationframework.driver import Driver
import os
from .safeflightautomationframework.page_objects.abstract_page.abstract_page import AbstractPage
from .safeflightautomationframework.page_objects.login_page.login_page import LoginPage
from .safeflightautomationframework.page_objects.flights_page.flights_page import FlightsPage
from .safeflightautomationframework.page_objects.create_flight_page.create_flight_page import CreateFlightPage
from .safeflightautomationframework.page_objects.delete_flight_page.delete_flight_page import DeleteFlightPage
from .safeflightautomationframework.page_objects.watch_list_page.watch_list_page import WatchListPage
from .safeflightautomationframework.page_objects.create_watch_list_entry_page.create_watch_list_entry_page import \
    CreateWatchListEntryPage
from .safeflightautomationframework.page_objects.delete_watch_list_entry_page.delete_watch_list_entry_page import \
    DeleteWatchListEntryPage

D = Driver
AP = AbstractPage
LP = LoginPage
FP = FlightsPage
CFP = CreateFlightPage
DFP = DeleteFlightPage
WLP = WatchListPage
CWLEP = CreateWatchListEntryPage
DWLEP = DeleteWatchListEntryPage


@pytest.fixture
def startup_driver():
    Driver.initialize()
    yield
    Driver.shutdown()


def test_bs_01(startup_driver):
    FlightsPage.go_to()
    page_source = Driver.get_page_source()
    soup = BeautifulSoup(page_source, 'lxml')
    highlighted_rows = soup.find_all("tr", class_="highlightRow")

    f = open(os.getcwd() + r"/zzz.txt", "w")
    f.write(str(highlighted_rows))
    f.close()

