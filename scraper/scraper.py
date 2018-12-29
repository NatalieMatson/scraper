import requests
import kivy
from bs4 import BeautifulSoup
kivy.require('1.10.1')

starting_url = requests.get('https://www.riderframesandgallery.com/')

if starting_url.status_code == requests.codes.ok:
  content = starting_url.content
else:
  print(starting_url.status_code)