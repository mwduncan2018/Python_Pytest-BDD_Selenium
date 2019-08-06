"""Step definitions for the Vetting Feature.

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

@scenario('Vetting.feature', 'Passenger schedules flight, passenger is not on the watch list')
def test_passenger_schedules_flight_passenger_is_not_on_the_watch_list():
    pass

@scenario('Vetting.feature', 'Passenger schedules flight, passenger is on the watch list')
def test_passenger_schedules_flight_passenger_is_on_the_watch_list():
    pass

@given('DSF navigates to the Login Page')
def dsf_navigates_to_the_login_page():
    LoginPage.go_to()

@given('logging in with a valid username and password combo')
def logging_in_with_a_valid_username_and_password_combo():
    LoginPage.login_as('mduncan').with_password('cucumber').submit_form()

@when('a passenger is added to the watch list')
def a_passenger_is_added_to_the_watch_list():
    CreateWatchListEntryPage.go_to()
    CreateWatchListEntryPage.create_entry().with_bounty(20000).with_first_name("Melissa").with_last_name("Angone").submit_form()

@when('a regular passenger schedules a flight')
def a_regular_passenger_schedules_a_flight():
    CreateFlightPage.go_to()
    CreateFlightPage.create_flight().with_arrival_airport('BWI').with_arrival_time('2/2/2019 11:00:00 AM').with_departure_airport('NYC').with_departure_time('2/2/2019 10:00:00 AM').with_first_name("Melissa").with_last_name("Angone").submit_form()

@when('a watched passenger schedules a flight')
def a_watched_passenger_schedules_a_flight():
    CreateFlightPage.go_to()
    CreateFlightPage.create_flight().with_arrival_airport('BWI').with_arrival_time('2/2/2019 11:00:00 AM').with_departure_airport('NYC').with_departure_time('2/2/2019 10:00:00 AM').with_first_name("Melissa").with_last_name("Angone").submit_form()

@then('a watched passenger is checked on the Flights Page')
def a_watched_passenger_is_checked_on_the_flights_page():
    FlightsPage.go_to()
    assert FlightsPage.watch_list_is_checked_for('Angone', 'Melissa')

@then('a regular passenger is not checked on the Flights Page')
def a_passenger_is_not_checked_on_the_flights_page():
    FlightsPage.go_to()
    assert (False == FlightsPage.watch_list_is_checked_for('Alsup', 'Andy'))
