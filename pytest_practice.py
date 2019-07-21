import pytest
import sys, os
from .SFAF.driver import Driver
from .SFAF.page_objects.abstract_page.abstract_page import AbstractPage
from .SFAF.page_objects.login_page.login_page import LoginPage
from .SFAF.page_objects.flights_page.flights_page import FlightsPage
from .SFAF.page_objects.create_flight_page.create_flight_page import CreateFlightPage
from .SFAF.page_objects.delete_flight_page.delete_flight_page import DeleteFlightPage
from .SFAF.page_objects.watch_list_page.watch_list_page import WatchListPage
from .SFAF.page_objects.create_watch_list_entry_page.create_watch_list_entry_page import CreateWatchListEntryPage
from .SFAF.page_objects.delete_watch_list_entry_page.delete_watch_list_entry_page import DeleteWatchListEntryPage

D = Driver
AP = AbstractPage
LP = LoginPage
FP = FlightsPage
CFP = CreateFlightPage
DFP = DeleteFlightPage
WLP = WatchListPage
CWLEP = CreateWatchListEntryPage
DWLEP = DeleteWatchListEntryPage

x = 0
y = 0

@pytest.fixture
def startup_driver():
	Driver.initialize()
	yield
	Driver.shutdown()

#basic test
def test_successful_login(startup_driver):
	LoginPage.go_to()
	LoginPage.login_as('mduncan').with_password('cucumber').submit_form()
	assert FlightsPage.is_at(), "Error: Not at the Flights page"

#verify an exception is raised correctly
def test_is_at_with_exception(startup_driver):
	FlightsPage.go_to()
	with pytest.raises(Exception):
		CreateWatchListEntryPage.is_at_with_exception()

#parametrized test 1
@pytest.mark.parametrize("varA, varB, varC", [(1,2,3),(10,20,30)])	
def test_flights_page(varA, varB, varC):
	assert varA < varB, "error 1"
	assert varB < varC, "error 2"

#parametrized test 2
valid_login_test_data = [
	('eangone','achievedhappiness'),
	('tduncan','airforce1'),
	('sharford','michigan'),
	('gduncan','mommom'),
	('tkubin','captaincoke'),
]
@pytest.mark.parametrize("username, password", valid_login_test_data)
def test_successful_login_parametrized(username, password):
	Driver.init()
	LoginPage.go_to()
	LoginPage.login_as(username).with_password(password).submit_form()
	assert FlightsPage.is_at()
	Driver.shutdown()

#parametrized test 3
invalid_username_password_combo_test_data = [
	('xduncan','abc'),
	('xkubin','abc'),
	('xharford','abc'),
]
@pytest.mark.parametrize("username, password", invalid_username_password_combo_test_data)
def test_login_with_invalid_username_password_combination(username, password):
	Driver.init()
	LoginPage.go_to()
	LoginPage.login_as(username).with_password(password).submit_form()
	assert LoginPage.validation_username_password_combination_invalid()
	Driver.shutdown()

#parametrized test 4
valid_username_and_blank_password_test_data = [
	('mduncan',''),
	('tkubin',''),
	('sharford',''),
]
@pytest.mark.parametrize("username, password", valid_username_and_blank_password_test_data)
def test_login_with_valid_username_and_invalid_password(username, password):
	Driver.init()
	LoginPage.go_to()
	LoginPage.login_as(username).with_password(password).submit_form()
	assert LoginPage.password_validation_is_displayed()
	Driver.shutdown()

#parametrized test 5
blank_username_test_data = [
	('','abc'),
	('',''),
	('','xyz'),
]
@pytest.mark.parametrize("username, password", blank_username_test_data)
def test_login_with_blank_username(username, password):
	Driver.init()
	LoginPage.go_to()
	LoginPage.login_as(username).with_password(password).submit_form()
	assert LoginPage.username_validation_is_displayed()
	Driver.shutdown()