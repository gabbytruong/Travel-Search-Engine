#Gabby Truong - Final Project - SI206

import json
from bs4 import BeautifulSoup
import unittest
import requests
import secrets
from yelpapi import YelpAPI
import argparse
import sqlite3 as sqlite

#CACHE FOR NETSTATE
CACHE_FNAME_3 = 'netstate_cache.json'
try:
    cache_file_3 = open(CACHE_FNAME_3, 'r')
    cache_contents_3 = cache_file_2.read()
    CACHE_DICT_3 = json.loads(cache_contents_3)
    cache_file_2.close()
except:
    CACHE_DICT_3 = {}

def get_cached_netstate(baseurl):
    unique_ident = baseurl
    if unique_ident in CACHE_DICT_3:
        return CACHE_DICT_3[unique_ident]
    else:
        resp = requests.get(baseurl)
        CACHE_DICT_3[unique_ident] = json.loads(resp.text)
        f = open(CACHE_FNAME_3, 'w')
        dumped_json = json.dumps(CACHE_DICT_3)
        f.write(dumped_json)
        f.close()
        return CACHE_DICT_3[unique_ident]

#GET DATA
#Scrape data from netstate site and get top city in each state / population
#init_user_inp = input('Enter a state abbreviation(type help if needed): ')

#while init_user_inp != 'exit':
#    if init_user_inp == 'help':
        # print('Please enter one of the following state abbreviations:')
        # print('ak for Alaska')
        # print('al for Alabama')
        # print('ar for Arkansas')
        # print('az for Arizona')
        # print('ca for California')
        # print('co for Colorado')
        # print('ct for Connecticut')
        # print('dc for District of Columbia')
        # print('de for Delaware')
        # print('fl for Florida')
        # print('ga for Georgia')
        # print('hi for Hawaii')
        # print('ia for Iowa')
        # print('id for Idaho')
        # print('il for Illinois')
        # print('in for Indiana')
        # print('ks for Kansas')
        # print('ky for Kentucky')
        # print('la for Louisiana')
        # print('ma for Massachusetts')
        # print('md for Maryland')
        # print('me for Maine')
        # print('mi for Michigan')
        # print('mn for Minnesota')
        # print('mo for Missouri')
        # print('ms for Mississippi')
        # print('mt for Montana')
        # print('nc for North Carolina')
        # print('nd for North Dakota')
        # print('ne for Nebraska')
        # print('nh for New Hampshire')
        # print('nj for New Jersey')
        # print('nm for New Mexico')
        # print('nv for Nevada')
        # print('ny for New York')
        # print('oh for Ohio')
        # print('ok for Oklahoma')
        # print('or for Oregon')
        # print('pa for Pennsylvania')
        # print('ri for Rhode Island')
        # print('sc for South Carolina')
        # print('sd for South Dakota')
        # print('tn for Tennessee')
        # print('tx for Texas')
        # print('ut for Utah')
        # print('va for Virginia')
        # print('vt for Vermont')
        # print('wa for Washington')
        # print('wi for Wisconsin')
        # print('wv for West Virginia')
        # print('wy for Wyoming')
        # print(input('Enter a state abbreviation(type help if needed):'))
        ##HOW DO I GET IT TO KEEP RUNNING THRU
#    else:
        def get_netstate_data(state_abbr):
            init_user_inp = state_abbr
            baseurl = 'http://www.netstate.com/states/alma/{}_alma.htm'.format(state_abbr)
            #html = get_cached_netstate(baseurl).text
            resp = requests.get(baseurl).text
            soup = BeautifulSoup(resp, 'html.parser') #change resp to html when figured out cache
            soup.prettify()
            symbol_table =soup.find(id="symboltable")
            div = symbol_table.find('table')
            my_table= div.find('table')
            #print(my_table)
            tr = my_table.find_all('tr')[0]
            #print(tr)
            td = tr.find_all('td')[1:3]
            print(td)
            city_list = []
            for item in td:
                print(item.string)
            #command_resp = ((item.string)[0] + ', {}:' + (item.string)[1]).format(state_abbr)

#while user_inp != 'exit':
#    get_netstate_data({}).format(user_inp)

yelp_api = YelpAPI(secrets.API_KEY)

#YELP CACHE FOOD
search_results = yelp_api.search_query(category = 'Restaurant', location = 'Birmingham, AL') #.format(city) #add state
with open('yelp_cache.json', 'w') as CACHE_DICT:
    json.dump(search_results, CACHE_DICT)

# read the cached file and save it as a json object i can work with
with open('yelp_cache.json') as json_data:
    cached_file = json.load(json_data)

list_of_restaurants = []
for x in range(0, 5):
    list_of_restaurants.append(cached_file["businesses"][x])
    rating = cached_file["businesses"][x]["rating"]
    price = cached_file["businesses"][x]["price"]
    review_num = cached_file["businesses"][x]["review_count"]
    name = cached_file["businesses"][x]["alias"]
    loc = cached_file["businesses"][x]["location"]["display_address"]
    print(name.replace('-', ' ') + ' ' + str(loc))
    print('Rating: ' + str(rating))
    print('Number of reviews: ' + str(review_num))
    print('Price range: ' + str(price))
    print('---------------------------------------------------------')

#YELP CACHE HOTELS
search_results_2 = yelp_api.search_query(category = 'Hotels', location = 'Birmingham, AL') #.format(city)
with open('yelp_cache_2.json', 'w') as CACHE_DICT_2:
    json.dump(search_results_2, CACHE_DICT_2)

with open('yelp_cache_2.json') as json_data_2:
    cached_file_2 = json.load(json_data_2)

list_of_hotels = []
for x in range(0, 5):
	list_of_hotels.append(cached_file_2["businesses"][x])
    #rating = cached_file_2["businesses"][x]["rating"]
    #price = cached_file_2["businesses"][x]["price"]
    # review_num = cached_file_2["businesses"][x]["review_count"]
    # name = cached_file_2["businesses"][x]["alias"]
    # loc = cached_file_2["businesses"][x]["location"]["display_address"]
    # print(name.replace('-', ' ') + ' ' + str(loc))
    # print('Rating: ' + str(rating))
    # print('Number of reviews: ' + str(review_num))
    # print('Price range: ' + str(price))
    # print('---------------------------------------------------------')

 #PRINTING SAME AS ABOVE ???? NEED HOTELS 

class Yelp:
    def __init__(self, city= "No city", state= "No state"):
        self.city = city
        self.state = state



DBNAME = 'cities.db'
#load into db
def init_db():
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    statement = '''
        DROP TABLE IF EXISTS 'Cities';
    '''
    cur.execute(statement)
    conn.commit()

    statement = '''
        DROP TABLE IF EXISTS 'YelpResults';
    '''
    cur.execute(statement)
    conn.commit()

    statement = '''
        CREATE TABLE 'Cities' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'City' TEXT NOT NULL,
            'State' TEXT NOT NULL,
            'Population' INTEGER

        );
    '''
    cur.execute(statement)
    conn.commit()

    statement = '''
        CREATE TABLE 'YelpResults' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'City' TEXT NOT NULL,
            'State' TEXT NOT NULL,
            'Search Category' TEXT NOT NULL,
            'Rating' INTEGER NOT NULL,
            'Price' INTEGER NOT NULL,
            'Reviews' INTEGER NOT NULL
        );
    '''

    cur.execute(statement)
    conn.commit()
    conn.close()

# def populate_cities():
#     conn = sqlite3.connect(DBNAME)
#     cur = conn.cursor()
#
#     conn.commit()

#make list of all cities - give each one an ID and make a database w it and pop #


#make thing for yelp to select top 5 restaurants and top 5 hotel/travel


#interactive prompt pt 1
#user_resp = input('Enter a state abbreviation (or "help" for options): ')
state_dict = {
        'ak': 'Alaska',
        'al': 'Alabama',
        'ar': 'Arkansas',
        'az': 'Arizona',
        'ca': 'California',
        'co': 'Colorado',
        'ct': 'Connecticut',
        'dc': 'District of Columbia',
        'de': 'Delaware',
        'fl': 'Florida',
        'ga': 'Georgia',
        'hi': 'Hawaii',
        'ia': 'Iowa',
        'id': 'Idaho',
        'il': 'Illinois',
        'in': 'Indiana',
        'ks': 'Kansas',
        'ky': 'Kentucky',
        'la': 'Louisiana',
        'ma': 'Massachusetts',
        'md': 'Maryland',
        'me': 'Maine',
        'mi': 'Michigan',
        'mn': 'Minnesota',
        'mo': 'Missouri',
        'mp': 'Northern Mariana Islands',
        'ms': 'Mississippi',
        'mt': 'Montana',
        'na': 'National',
        'nc': 'North Carolina',
        'nd': 'North Dakota',
        'ne': 'Nebraska',
        'nh': 'New Hampshire',
        'nj': 'New Jersey',
        'nm': 'New Mexico',
        'nv': 'Nevada',
        'ny': 'New York',
        'oh': 'Ohio',
        'ok': 'Oklahoma',
        'or': 'Oregon',
        'pa': 'Pennsylvania',
        'pr': 'Puerto Rico',
        'ri': 'Rhode Island',
        'sc': 'South Carolina',
        'sd': 'South Dakota',
        'tn': 'Tennessee',
        'tx': 'Texas',
        'ut': 'Utah',
        'va': 'Virginia',
        'vi': 'Virgin Islands',
        'vt': 'Vermont',
        'wa': 'Washington',
        'wi': 'Wisconsin',
        'wv': 'West Virginia',
        'wy': 'Wyoming'
}


#plotly with price??
