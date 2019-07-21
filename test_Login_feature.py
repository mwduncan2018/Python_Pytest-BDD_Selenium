"""Login feature tests."""
import pytest
from pytest_bdd import (
    scenario,
    given,
    when,
    then,
    parsers,
)
import sys, os
from .safe_flight_automation_framework.driver import Driver
from .safe_flight_automation_framework.page_objects.abstract_page.abstract_page import AbstractPage
from .safe_flight_automation_framework.page_objects.login_page.login_page import LoginPage
from .safe_flight_automation_framework.page_objects.flights_page.flights_page import FlightsPage
from .safe_flight_automation_framework.page_objects.create_flight_page.create_flight_page import CreateFlightPage
from .safe_flight_automation_framework.page_objects.delete_flight_page.delete_flight_page import DeleteFlightPage
from .safe_flight_automation_framework.page_objects.watch_list_page.watch_list_page import WatchListPage
from .safe_flight_automation_framework.page_objects.create_watch_list_entry_page.create_watch_list_entry_page import CreateWatchListEntryPage
from .safe_flight_automation_framework.page_objects.delete_watch_list_entry_page.delete_watch_list_entry_page import DeleteWatchListEntryPage

D = Driver
AP = AbstractPage
LP = LoginPage
FP = FlightsPage
CFP = CreateFlightPage
DFP = DeleteFlightPage
WLP = WatchListPage
CWLEP = CreateWatchListEntryPage
DWLEP = DeleteWatchListEntryPage

#This fixture is given to each scenario to startup and shutdown the browser.
@pytest.fixture
def startup_shutdown_driver():
    Driver.init()
    yield
    Driver.shutdown()

@scenario('Login.feature', 'Login with a valid username and password')
def test_login_with_a_valid_username_and_password(startup_shutdown_driver):
    """Login with a valid username and password."""
    pass

@given('the webdriver is initialized')
def the_webdriver_is_initialized():
    pass

@given('DSF navigates to the Login Page')
def dsf_navigates_to_the_login_page():
    LoginPage.go_to()

@when('logging in with a valid username and password combo')
def logging_in_with_a_valid_username_and_password_combo():
    LoginPage.login_as('mduncan').with_password('cucumber').submit_form()

@then('DSF is at the Flights Page')
def dsf_is_at_the_flights_page():
    assert FlightsPage.is_at()

@then('DSF is not at the Login Page')
def dsf_is_not_at_the_login_page():
    assert LoginPage.is_at() == False


@scenario('Login.feature', 'Login with a valid username and password Parametrized')
def test_login_with_a_valid_username_and_password__parametrized(startup_shutdown_driver):
    pass

@when('logging in as username <username> and password <password>')
def logging_in_as_username_and_password(username, password):
    LoginPage.login_as(username).with_password(password).submit_form()