import pytest

import sys, os
import SFAF

x = 0
y = 0

@pytest.fixture
def startup_driver():
	Driver.initialize()
	yield
	Driver.shutdown()
	
def test_login_page(startup_driver):
	LoginPage.go_to()
	LoginPage.login_as('mduncan').with_password('cucumber').submit_form()
	assert FlightsPage.is_at(), "Error: Not at the Flights page"

@pytest.mark.parametrize("varA, varB, varC", [(1,2,3),(10,20,30)])	
def test_flights_page(varA, varB, varC):
	assert varA < varB, "error 1"
	assert varB < varC, "error 2"