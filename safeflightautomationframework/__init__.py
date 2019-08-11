from .driver import Driver
from .page_objects.abstract_page.abstract_page import AbstractPage
from .page_objects.login_page.login_page import LoginPage
from .page_objects.flights_page.flights_page import FlightsPage
from .page_objects.create_flight_page.create_flight_page import CreateFlightPage
from .page_objects.delete_flight_page.delete_flight_page import DeleteFlightPage
from .page_objects.watch_list_page.watch_list_page import WatchListPage
from .page_objects.create_watch_list_entry_page.create_watch_list_entry_page import CreateWatchListEntryPage
from .page_objects.delete_watch_list_entry_page.delete_watch_list_entry_page import DeleteWatchListEntryPage

D = Driver
AP = AbstractPage
LP = LoginPage
FP = FlightsPage
CFP = CreateFlightPage
DFP = DeleteFlightPage
WLP = WatchListPage
CWLEP = CreateWatchListEntryPage
DWLEP = DeleteWatchListEntryPage