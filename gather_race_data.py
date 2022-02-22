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


# Function that gets the date of the race
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
# Function to get the number of finishers
def get_number_of_finishers(table_row):
    type_finishers_location_tr = table_row.select_one('td:nth-of-type(2)')
    text =  type_finishers_location_tr.select_one('div:nth-of-type(2)').text
    arr = text.split('/')
    finishers = arr[1]
    return finishers
# Function to get the location of the race
def get_race_location(table_row):
    type_finishers_location_tr = table_row.select_one('td:nth-of-type(2)')
    text =  type_finishers_location_tr.select_one('div:nth-of-type(2)').text
    arr = text.split('/')
    location = arr[2]
    return location
# Function to gather race results -- returns a dataframe with all of the data
def gather_race_results():
    # Creating a dictionary to save the collected data to
    data = {
        'date': [],
        'name': [],
        'type': [],
        'finishers': [],
        'location': []
    }
    # Setting initial page number for looping through the URLs
    page_number = 1
    # For loop to loop through 1000 web pages
    while page_number <= 1000:
        # URL in an fstring to apply the page number to the URL
        URL = f'https://calendar.ultrarunning.com/race-results?page={page_number}'
        # Get request to the web server
        WEBPAGE = requests.get(URL)
        # Parsing with beautiful soup
        soup = BeautifulSoup(WEBPAGE.content, 'html5lib')
        # Array of table rows with the race class
        race_trs = soup.find_all('tr', {'class': 'race'})
        # Looping through all of the trs with the class of race
        for i in race_trs:
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
        # Increment page number by 1
        page_number += 1
    # Return the complete dataframe
    return pandas.DataFrame(data)
# Setting variable equal to the dataframe of race data
dataframe = gather_race_results()
# Saving the dataframe to a CSV  file
dataframe.to_csv('ultra_marathon_race_results.csv')

