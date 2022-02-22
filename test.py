import pandas
import requests
from bs4 import BeautifulSoup
dataframe = pandas.read_csv('race_results_urls.csv')


def get_placement(url):
    WEBPAGE = requests.get(url)
    # Parsing with beautiful soup
    soup = BeautifulSoup(WEBPAGE.content, 'html5lib')
    race_trs = soup.find_all('tr')
    placement = []
    for i in race_trs:
        finishers = i.select_one('td:nth-of-type(1)').text
        placement.append(finishers)
    placement = [x.replace(" ", "") for x in placement]
    counter = 1
    while counter <= 40:
        placement.pop()
        counter += 1
    new_placement = []
    for i in placement:
        new_placement.append(i.strip())
    return new_placement
def get_gender(url):
    WEBPAGE = requests.get(url)
    # Parsing with beautiful soup
    soup = BeautifulSoup(WEBPAGE.content, 'html5lib')
    race_trs = soup.find_all('tr')
    gender = soup.find_all('div', {'class': 'tw-font-light'})
    gender_age_arr = []
    for i in gender:
        string = str(i)
        new_str = string.replace('<div class="tw-font-light">', "")
        new_new = new_str.replace('</div>', "")
        final = new_new.replace('<div class="tw-pr-1 tw-font-light">', "")

        gender_age_arr.append(final)
    gender = []
    gender.append(gender_age_arr[0::2])
    return gender
def get_race_name(url):
    WEBPAGE = requests.get(url)
    # Parsing with beautiful soup
    soup = BeautifulSoup(WEBPAGE.content, 'html5lib')
    race_trs = soup.find_all('tr')
    return soup.find('title').text
def get_age(url):
    WEBPAGE = requests.get(url)
    # Parsing with beautiful soup
    soup = BeautifulSoup(WEBPAGE.content, 'html5lib')
    race_trs = soup.find_all('tr')

    gender = soup.find_all('div', {'class': 'tw-font-light'})
    gender_age_arr = []
    for i in gender:
        string = str(i)
        new_str = string.replace('<div class="tw-font-light">', "")
        new_new = new_str.replace('</div>', "")
        final = new_new.replace('<div class="tw-pr-1 tw-font-light">', "")

        gender_age_arr.append(final)
    age = []
    age=gender_age_arr[1::2]

    return age
def get_name(url):
    WEBPAGE = requests.get(url)
    # Parsing with beautiful soup
    soup = BeautifulSoup(WEBPAGE.content, 'html5lib')
    race_trs = soup.find_all('tr')

    new_counter = 1
    names = []
    for i in race_trs:
        finishers = str(i.select_one('a').text)
        names.append(finishers.strip())

    while new_counter <= 40:
        names.pop()
        new_counter += 1
    return names



def get_racer_data():
    data = {
        'race': [],
        'name': [],
        'placement': [],
        'gender': [],
        'age': []
    }
    page_number=1
    while page_number<=len(dataframe['0'][0:50]):
        url = dataframe['0'][page_number]
        data['race'].append(get_race_name(url))
        data['name'].append(get_name(url))
        data['placement'].append(get_placement(url))
        data['gender'].append(get_gender(url))
        data['age'].append(get_age(url))
        page_number+=1
    return pandas.DataFrame(data)

results = get_racer_data()

print(results)

results.to_csv('individual_race_data.csv')