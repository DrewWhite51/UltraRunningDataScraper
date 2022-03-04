import pandas as pd
import pandas
from Race import Race
from pymongo import MongoClient
import pprint

results_dataframe = pandas.read_csv('race_results_urls.csv')

firstRace = Race('https://calendar.ultrarunning.com/event/hundred-in-the-hood/race/1096/results')

def create_dataframe(race_url):
    try:
        data = {
            # 'raceName': [],
            'racePlacements': [],
            'genders': [],
            'ages': [],
            'names': []
        }

        race = Race(race_url)
        data['racePlacements'] = (race.get_placements())
        data['genders'] = (race.get_genders())
        data['ages'] = (race.get_ages())
        data['names'] = (race.get_names())
        data['raceName'] = race.get_race_name()
        
        print(len(data['genders']))
        print(len(data['ages']))
        print(len(data['names']))
        print(len(data['racePlacements']))
        # print(len(data['raceName']))
        
        return data
    
    except:
        print('Error with')
        print(race_url)
        
    



