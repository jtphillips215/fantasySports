# importing dependencies
from bs4 import BeautifulSoup
import requests

# base URL as site uses RESTful scheme
BASE_URL = 'http://racing-reference.info/driver-loop-data-stats/'

# sending html request to get site data
# were just ugly concatonating the url here as a test, will be set programatically later
url = BASE_URL + 'truexma02/W/2022/'
page = requests.get(url)

# creating our soup to parse
soup = BeautifulSoup(page.content, 'html.parser')

# testing data flow is successful
print(soup)
