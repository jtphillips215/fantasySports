# importing dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd

# base URL as site uses RESTful scheme
BASE_URL = 'https://www.racing-reference.info/loopdata/'

# setting years as range for next gen car, setting races as a range of race numbers from 1 to 36
years = range(2022, 2024)
races = range(1, 37)

# iterating over each race during each year
for year in years:
    for race in races:
        if race < 10:
            url = BASE_URL + f'{year}-0{race}/W/'
        else:
            url = BASE_URL + f'{year}-{race}/W/'

        # sending html request to get site data
        page = requests.get(url)
        # creating soup to parse
        soup = BeautifulSoup(page.text, 'html.parser')

        data_frames = pd.read_html(page.text)
