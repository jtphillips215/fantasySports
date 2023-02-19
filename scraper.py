# importing dependencies
from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape(url):
    # sending html request to get site data
    page = requests.get(url)
    # creating soup to parse
    soup = BeautifulSoup(page.text, 'html.parser')

    # using pandas to read html and create data frame to return that data to main
    data_frame = pd.read_html(page.text)
    return data_frame
