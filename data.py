#!/bin/python3
import requests
from bs4 import BeautifulSoup
url = 'https://www.findandtrace.com/trace-mobile-number-location'
#url = 'http://127.0.0.1:8888/h.html'
data = { 'mobilenumber' : '9798092707'}
response = requests.post(url, json=data)
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('b')
for x in list(dict.fromkeys(headlines)):
#    if x.text.strip() == "LIVE - Active":
        print(x.text.strip())
