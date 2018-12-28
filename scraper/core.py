import requests
from bs4 import BeautifulSoup

starting_url = requests.get('https://www.riderframesandgallery.com/')

if starting_url.status_code == requests.codes.ok:
  content = starting_url.content
else:
  print(starting_url.status_code)