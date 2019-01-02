import requests
from bs4 import BeautifulSoup
import sys
from docx import Document
import os

url = input('Site URL - Include http://www. : ')
current_url = requests.get(url)

if current_url.status_code == requests.codes.ok:
  content = current_url.content
else:
  print(current_url.status_code)
  sys.exit()

soup = BeautifulSoup(content, 'html.parser')

document = Document()
filepath = '../results/'
folder = input('Name of root folder to output results to: ')
if os.path.isdir('{0}{1}'.format(filepath, folder)):
  document.save('{0}{1}/test.docx'.format(filepath, folder))
else:
  os.mkdir('../results/{}'.format(folder))
  document.save('{0}{1}/test.docx'.format(filepath, folder))