import pandas
from bs4 import BeautifulSoup
import re
import requests
from selenium import webdriver
import pprint as pp




page_number=1
# URL for race results
URL = 'https://calendar.ultrarunning.com/race-results'
# Get request for the webpage
WEBPAGE = requests.get(URL)
# Parsing with beautiful soup
soup = BeautifulSoup(WEBPAGE.content, 'lxml')
# Array of table rows with the race class
race_trs = soup.find_all('tr', {'class':'race'})

url_list = []
i = 0
while i <=19:
    ele = soup.select('tr')[i]
    on_click = ele.get('onclick')
    new_str = on_click.replace("window.location.href='","")
    url = new_str.replace("'","")
    url_list.append(url)
    i +=1



page_number = 1
while page_number <= 1000:
    URL = f'https://calendar.ultrarunning.com/race-results?page={page_number}'
    WEBPAGE = requests.get(URL)
    # Parsing with beautiful soup
    soup = BeautifulSoup(WEBPAGE.content, 'lxml')
    i = 0
    while i <= 19:
        ele = soup.select('tr')[i]
        on_click = ele.get('onclick')
        new_str = on_click.replace("window.location.href='", "")
        url = new_str.replace("'", "")
        url_list.append(url)
        i += 1

    page_number+=1

dataframe = pandas.DataFrame(url_list)

print(dataframe)
dataframe.to_csv('race_results_urls.csv')











