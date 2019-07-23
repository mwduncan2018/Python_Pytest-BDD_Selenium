"""Step definitions for the Login Feature.

Usage:
    Generate a report in Cucumber JSON format by executing pytest in the same directory as this file.
    pytest --cucumberjson=<path>
    pytest --cucumberjson=C:/dev/Python/python_selenium_automation_framework/pytest_bdd_results/results_01.json
"""
import pytest
import sys, os
from pytest_bdd import scenario, given, when, then, parsers
from .safe_flight_automation_framework.driver import Driver
from .safe_flight_automation_framework.page_objects.abstract_page.abstract_page import AbstractPage
from .safe_flight_automation_framework.page_objects.login_page.login_page import LoginPage
from .safe_flight_automation_framework.page_objects.flights_page.flights_page import FlightsPage
from .safe_flight_automation_framework.page_objects.create_flight_page.create_flight_page import CreateFlightPage
from .safe_flight_automation_framework.page_objects.delete_flight_page.delete_flight_page import DeleteFlightPage
from .safe_flight_automation_framework.page_objects.watch_list_page.watch_list_page import WatchListPage
from .safe_flight_automation_framework.page_objects.create_watch_list_entry_page.create_watch_list_entry_page import CreateWatchListEntryPage
from .safe_flight_automation_framework.page_objects.delete_watch_list_entry_page.delete_watch_list_entry_page import DeleteWatchListEntryPage

#This fixture is given to each scenario to startup and shutdown the browser.
@pytest.fixture
def startup_shutdown_driver():
    Driver.init()
    yield
    Driver.shutdown()

@scenario('Login.feature', 'Login, blank username, blank password')
def test_login_blank_username_blank_password(startup_shutdown_driver):
    pass

@scenario('Login.feature', 'Login, valid username, valid password')
def test_login_valid_username_valid_password(startup_shutdown_driver):
    pass

@scenario('Login.feature', 'Parametrized Login, invalid username and password combination')
def test_parametrized_login_invalid_username_and_password_combination(startup_shutdown_driver):
    pass

@scenario('Login.feature', 'Parametrized Login, valid username, valid password')
def test_parametrized_login_valid_username_valid_password(startup_shutdown_driver):
    pass

@given('DSF navigates to the Login Page')
def dsf_navigates_to_the_login_page():
    LoginPage.go_to()

@when('attempting to login with blank username and password fields')
def attempting_to_login_with_blank_username_and_password_fields():
    LoginPage.login_as('').with_password('').submit_form()

@when('logging in as username <username> and password <password>')
def logging_in_as_username_and_password(username, password):
    LoginPage.login_as(username).with_password(password).submit_form()

@when('logging in with a valid username and password combo')
def logging_in_with_a_valid_username_and_password_combo():
    LoginPage.login_as('mduncan').with_password('cucumber').submit_form()

@then('DSF is at the Flights Page')
def dsf_is_at_the_flights_page():
    assert FlightsPage.is_at() == True

@then('DSF is not at the Login Page')
def dsf_is_not_at_the_login_page():
    assert LoginPage.is_at() == False

@then('validation for an invalid username and password combination is displayed')
def validation_for_an_invalid_username_and_password_combination_is_displayed():
    assert LoginPage.validation_username_password_combination_invalid() == True

@then('validation is displayed that states the password is required')
def validation_is_displayed_that_states_the_password_is_required():
    assert LoginPage.password_validation_is_displayed() == True

@then('validation is displayed that states the username is required')
def validation_is_displayed_that_states_the_username_is_required():
    assert LoginPage.username_validation_is_displayed() == True