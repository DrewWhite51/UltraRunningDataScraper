import pprint
import pandas
from bs4 import BeautifulSoup
import requests


dataframe = pandas.read_csv('race_results_urls.csv')



page_number=1
# URL for race results
URL = dataframe['0'][500]
# Get request for the webpage
WEBPAGE = requests.get(URL)
# Parsing with beautiful soup
soup = BeautifulSoup(WEBPAGE.content, 'html5lib')
# Dictionary to save data to
data = {
    'race': [],
    'name': [],
    'placement': [],
    'gender': [],
    'age': []
}
# Selecting the TRs that I need
race_trs = soup.find_all('tr')

placement = []
for i in race_trs:
    finishers = i.select_one('td:nth-of-type(1)').text
    placement.append(finishers)
placement = [x.replace(" ", "") for x in placement]
counter = 1
while counter <=40:
    placement.pop()
    counter+=1

for i in placement:
    data['placement'].append(i.strip())


gender = soup.find_all('div', {'class':'tw-font-light'})
gender_age_arr = []
for i in gender:
    string = str(i)
    new_str = string.replace('<div class="tw-font-light">', "")
    new_new = new_str.replace('</div>', "")
    final = new_new.replace('<div class="tw-pr-1 tw-font-light">', "")

    gender_age_arr.append(final)
data['age'] = (gender_age_arr[1::2])
data['gender']=(gender_age_arr[0::2])



new_counter = 1
names = []
for i in race_trs:
    finishers = str(i.select_one('a').text)
    names.append(finishers.strip())

while new_counter <=40:
    names.pop()
    new_counter+=1
data['name']=names
data['race'] = soup.find('title').text
print(URL)

results = pandas.DataFrame(data)

print(results)


    



