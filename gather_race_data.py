import pprint
import pandas
from bs4 import BeautifulSoup
import requests

page_number=1
# URL for race results
URL = 'https://calendar.ultrarunning.com/race-results'
# Get request for the webpage
WEBPAGE = requests.get(URL)
# Parsing with beautiful soup
soup = BeautifulSoup(WEBPAGE.content, 'html5lib')
# Array of table rows with the race class
race_trs = soup.find_all('tr', {'class':'race'})



def get_race_date(table_row):
    date_td = table_row.select_one('td:nth-of-type(1)')
    month = date_td.select_one('div:nth-of-type(1)').text
    day = date_td.select_one('div:nth-of-type(2)').text
    year = date_td.select_one('div:nth-of-type(3)').text
    date_string = f'{month}/{day}/{year}'
    return date_string
# Function to get the name of a race for a race class that is passed
def get_race_name(table_row):
    name_td = table_row.select_one('td:nth-of-type(2)')
    return name_td.select_one('div:nth-of-type(1)').text
# Function to get the race type / finishers / Location
def get_race_type(table_row):
    type_finishers_location_tr = table_row.select_one('td:nth-of-type(2)')
    text =  type_finishers_location_tr.select_one('div:nth-of-type(2)').text
    arr = text.split('/')
    race_type = arr[0]
    return race_type
def get_number_of_finishers(table_row):
    type_finishers_location_tr = table_row.select_one('td:nth-of-type(2)')
    text =  type_finishers_location_tr.select_one('div:nth-of-type(2)').text
    arr = text.split('/')
    finishers = arr[1]
    return finishers
def get_race_location(table_row):
    type_finishers_location_tr = table_row.select_one('td:nth-of-type(2)')
    text =  type_finishers_location_tr.select_one('div:nth-of-type(2)').text
    arr = text.split('/')
    location = arr[2]
    return location


def gather_race_results():
    data = {
        'date': [],
        'name': [],
        'type': [],
        'finishers': [],
        'location': []
    }
    page_number = 1
    while page_number <= 1000:
        URL = f'https://calendar.ultrarunning.com/race-results?page={page_number}'
        WEBPAGE = requests.get(URL)
        # Parsing with beautiful soup
        soup = BeautifulSoup(WEBPAGE.content, 'html5lib')
        # Array of table rows with the race class
        race_trs = soup.find_all('tr', {'class': 'race'})
        for i in race_trs:
            # print('---------------')
            # print(get_race_date(i).strip())
            data['date'].append(get_race_date(i).strip())
            # print(get_race_name(i).strip())
            data['name'].append(get_race_name(i).strip())
            # print(get_race_type(i).strip())
            data['type'].append(get_race_type(i).strip())
            # print(get_number_of_finishers(i).strip())
            data['finishers'].append(get_number_of_finishers(i).strip())
            # print(get_race_location(i).strip())
            data['location'].append(get_race_location(i).strip())

        page_number += 1



    return pandas.DataFrame(data)

dataframe = gather_race_results()

dataframe.to_csv('ultra_marathon_race_results.csv')

