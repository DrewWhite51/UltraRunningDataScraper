import requests
import pandas
from urllib.parse import urlencode

dataframe = pandas.read_csv('race_results_urls.csv')
urls = dataframe['0']
KEY = 'b47eaa17dc56908f412b0195c7abf9a8'

# for url in urls:
#     params = {'api_key': KEY, 'url': url}
#     response = requests.get('http://api.scraperapi.com/', params=urlencode(params))
#     print(response.text)


individual_race_data = pandas.read_csv('individual_race_data.csv')


