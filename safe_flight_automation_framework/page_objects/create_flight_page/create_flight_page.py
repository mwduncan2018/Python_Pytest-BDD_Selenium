#!/usr/bin/env python3
"""Page-object model for the create flight page.
"""

import sys
from ..driver import Driver
from .abstract_page import AbstractPage

class CreateFlightCommand():

	def __init__(self):
		self._departure_airport = None
		self._arrival_airport = None
		self._departure_time = None
		self._arrival_time = None
		self._first_name = None
		self._last_name = None
	
	def with_departure_airport(self, driver, departure_airport):
		self._departure_airport = departure_airport

	def with_arrival_airport(self, driver, arrival_airport):
		self._arrival_airport = arrival_airport

	def with_departure_time(self, driver, departure_time):
		self._departure_time = departure_time

	def with_arrival_time(self, driver, arrival_time):
		self._arrival_time = arrival_time

	def with_first_name(self, driver, first_name):
		self._first_name = first_name

	def with_last_name(self, driver, last_name):
		self._last_name = last_name

	def submit(self, driver):
		driver.find_element_by_id("DepartureAirport").send_keys(self._departure_airport)
		driver.find_element_by_id("ArrivalAirport").send_keys(self._arrival_airport)
		driver.find_element_by_id("DepartureTime").send_keys(self._departure_time)
		driver.find_element_by_id("ArrivalTime").send_keys(self._arrival_time)
		driver.find_element_by_id("FirstName").send_keys(self._first_name)
		driver.find_element_by_id("LastName").send_keys(self._last_name)
		driver.find_element_by_id("btnCreate").click()


class CreateFlightPage(AbstractPage):

	def __init__(self, driver):
		super().__init__()
		self._page_name = "Create Flight"

	def is_at(self, driver):
		super().is_at()

	def create_flight(self, driver):
		self.is_at()
		Driver.instance.navigate().to(self._url + 'Flights/Create')


if __name__ == '__main__':
	print("Executing main")