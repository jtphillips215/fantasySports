# importing dependencies
from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com/'
page = requests.get(url)

print(page)
