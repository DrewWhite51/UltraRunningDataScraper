import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode


class Race:

    def __init__(self, url):
        self.url = url


    def get_race_name(self):
       KEY = 'b47eaa17dc56908f412b0195c7abf9a8'
       params = {'api_key': KEY, 'url': self.url}
       response = requests.get('http://api.scraperapi.com/', params=urlencode(params))
       soup = BeautifulSoup(response.content, 'html5lib')
       return soup.find('title').text

    def get_placements(self):
        KEY = 'b47eaa17dc56908f412b0195c7abf9a8'
        params = {'api_key': KEY, 'url': self.url}
        response = requests.get('http://api.scraperapi.com/', params=urlencode(params))
        soup = BeautifulSoup(response.content, 'html5lib')
        race_trs = soup.find_all('tr')
        placement = []
        for i in race_trs:
            finishers = i.select_one('td:nth-of-type(1)').text
            placement.append(finishers)
        placement = [x.replace(" ", "") for x in placement]
        placement = [x.replace("\n", "") for x in placement]
        counter = 1
        while counter <= 40:
            placement.pop()
            counter += 1
        return placement

    def get_genders(self):
        KEY = 'b47eaa17dc56908f412b0195c7abf9a8'
        params = {'api_key': KEY, 'url': self.url}
        response = requests.get('http://api.scraperapi.com/', params=urlencode(params))
        soup = BeautifulSoup(response.content, 'html5lib')
        race_trs = soup.find_all('tr')
        gender = soup.find_all('div', {'class': 'tw-font-light'})
        gender_age_arr = []
        for i in gender:
            string = str(i)
            new_str = string.replace('<div class="tw-font-light">', "")
            new_new = new_str.replace('</div>', "")
            final = new_new.replace('<div class="tw-pr-1 tw-font-light">', "")
            gender_age_arr.append(final)
        return (gender_age_arr[0::2])

    def get_ages(self):
        KEY = 'b47eaa17dc56908f412b0195c7abf9a8'
        params = {'api_key': KEY, 'url': self.url}
        response = requests.get('http://api.scraperapi.com/', params=urlencode(params))
        soup = BeautifulSoup(response.content, 'html5lib')
        race_trs = soup.find_all('tr')
        gender = soup.find_all('div', {'class': 'tw-font-light'})
        gender_age_arr = []
        for i in gender:
            string = str(i)
            new_str = string.replace('<div class="tw-font-light">', "")
            new_new = new_str.replace('</div>', "")
            final = new_new.replace('<div class="tw-pr-1 tw-font-light">', "")
            gender_age_arr.append(final)
        return (gender_age_arr[1::2])

    def get_names(self):
        KEY = 'b47eaa17dc56908f412b0195c7abf9a8'
        params = {'api_key': KEY, 'url': self.url}
        response = requests.get('http://api.scraperapi.com/', params=urlencode(params))
        soup = BeautifulSoup(response.content, 'html5lib')
        race_trs = soup.find_all('tr')
        counter = 1
        names = []
        for i in race_trs:
            finishers = str(i.select_one('a').text)
            names.append(finishers.strip())
        while counter <= 40:
            names.pop()
            counter += 1
        return names