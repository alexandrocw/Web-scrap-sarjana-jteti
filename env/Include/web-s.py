from bs4 import BeautifulSoup
import requests
import re
from time import sleep

sleep(60)

page = requests.get('http://sarjana.jteti.ugm.ac.id/akademik')

soup = BeautifulSoup(page.content, features='html.parser')

item = soup.find('tr')

print(item.get_text())