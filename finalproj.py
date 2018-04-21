#Gabby Truong - Final Project - SI206

import json
from bs4 import BeautifulSoup
import unittest
import requests
import secrets
from yelpapi import YelpAPI
import sqlite3 as sqlite
import plotly
import plotly.plotly as py
import plotly.graph_objs as go

#upload  to plotly ( screenshots)

yelp_api = YelpAPI(secrets.API_KEY)

plotly.tools.set_credentials_file(username='gtruong', api_key= secrets.PLOT_KEY)


#CACHE FOR NETSTATE
NETSTATE_CACHE = 'netstate_cache.json'

try:
    cache_file_3 = open(NETSTATE_CACHE, 'r')
    cache_contents_3 = cache_file_3.read()
    CACHE_DICT_3 = json.loads(cache_contents_3)
    cache_file_3.close()
except:
    CACHE_DICT_3 = {}

def get_cached_netstate(baseurl):
    unique_ident = baseurl
    if unique_ident in CACHE_DICT_3.keys():
        return CACHE_DICT_3[unique_ident]
    else:
        resp = requests.get(baseurl)
        CACHE_DICT_3[unique_ident] = resp.text
        f = open(NETSTATE_CACHE, 'w')
        dumped_json = json.dumps(CACHE_DICT_3)
        f.write(dumped_json)
        f.close()
        return CACHE_DICT_3[unique_ident]

#INITIAL PROMPT FOR USER INPUT
user_inp = input('Please enter a state abbreviation (or enter "help" for a list of states): ')

#ADDING A HELP OPTION
if user_inp == 'help':
     print('Please enter one of the following state abbreviations:')
     print('ak for Alaska')
     print('al for Alabama')
     print('ar for Arkansas')
     print('az for Arizona')
     print('ca for California')
     print('co for Colorado')
     print('ct for Connecticut')
     print('de for Delaware')
     print('fl for Florida')
     print('ga for Georgia')
     print('hi for Hawaii')
     print('ia for Iowa')
     print('id for Idaho')
     print('il for Illinois')
     print('in for Indiana')
     print('ks for Kansas')
     print('ky for Kentucky')
     print('la for Louisiana')
     print('ma for Massachusetts')
     print('md for Maryland')
     print('me for Maine')
     print('mi for Michigan')
     print('mn for Minnesota')
     print('mo for Missouri')
     print('ms for Mississippi')
     print('mt for Montana')
     print('nc for North Carolina')
     print('nd for North Dakota')
     print('ne for Nebraska')
     print('nh for New Hampshire')
     print('nj for New Jersey')
     print('nm for New Mexico')
     print('nv for Nevada')
     print('ny for New York')
     print('oh for Ohio')
     print('ok for Oklahoma')
     print('or for Oregon')
     print('pa for Pennsylvania')
     print('ri for Rhode Island')
     print('sc for South Carolina')
     print('sd for South Dakota')
     print('tn for Tennessee')
     print('tx for Texas')
     print('ut for Utah')
     print('va for Virginia')
     print('vt for Vermont')
     print('wa for Washington')
     print('wi for Wisconsin')
     print('wv for West Virginia')
     print('wy for Wyoming')
     user_inp = input('Please enter a state abbreviation: ')

#CREATE NETSTATE CLASS
class NetState:
    def __init__(self, state_abbr='No state', city='No city',
    population ='No population', rating = 'No rating',
    price = 'No price range', review_num = 'No review number' ,
    name= 'No business name' , address = 'No address'):

        self.state_abbr = user_inp
        self.rating = rating
        self.price = price
        self.review_num = review_num
        self.name = name
        self.address = address
        self.city = city
        self.population = population


    def __str__(self):
        return '{}, {}: {}'.format(city, state_abbr, population)

    print(' ')

#GET NETSTATE DATA
def get_netstate_data(user_inp):
    baseurl = 'http://www.netstate.com/states/alma/{}_alma.htm'.format(user_inp)
    html = get_cached_netstate(baseurl)
    soup = BeautifulSoup(html, 'html.parser')
    container =soup.find(id='container')
    my_table = container.find('table')
    inner_table = my_table.find('table')
    tr = inner_table.find_all('tr')[0]
    td = tr.find_all('td')
    city = td[1].string
    population = td[2].string
    class_item = NetState(city = city, population = population, state_abbr = user_inp)

    print(city + ', ' + user_inp.upper() + ': population of ' + population + '\n ')
    return (city, user_inp, population)

get_netstate_data(user_inp) #PRINT RESULT STRING


#YELP CACHE - FOOD
def get_restaurants(user_inp):
    city = get_netstate_data(user_inp)
    search_results = yelp_api.search_query(term = 'Restaurant',
    location = str(city) + ', ' + str(user_inp.upper()))
    with open('yelp_cache.json', 'w') as CACHE_DICT:
        json.dump(search_results, CACHE_DICT)

    with open('yelp_cache.json') as json_data: # read the cached file and save it as a json object i can work with
        cached_file = json.load(json_data)

    for x in range(0, 5):
        try:
            rating = cached_file["businesses"][x]["rating"]
        except:
            rating = "No rating available."
        try:
            price = cached_file["businesses"][x]["price"]
        except:
            price = "No price range available."
        review_num = cached_file["businesses"][x]["review_count"]
        name = cached_file["businesses"][x]["alias"]
        address = cached_file["businesses"][x]["location"]["display_address"]
        print('------------------- Restaurant -------------------')
        print(name.replace('-', ' ').upper() + ' ' + str(address))
        print('Rating: ' + str(rating))
        print('Number of reviews: ' + str(review_num))
        print('Price range: ' + str(price))
        print('')
    return (name.replace('-', ' '), str(address), str(rating), str(review_num), str(price))

#YELP CACHE - HOTELS
def get_hotels(user_inp):
    city = get_netstate_data(user_inp)
    search_results_2 = yelp_api.search_query(term = 'Hotels',
    location = str(city) + ', ' + str(user_inp.upper()))

    with open('yelp_cache_2.json', 'w') as CACHE_DICT_2:
        json.dump(search_results_2, CACHE_DICT_2)

    with open('yelp_cache_2.json') as json_data_2:
        cached_file_2 = json.load(json_data_2)

    for x in range(0, 5):
        rating = cached_file_2["businesses"][x]["rating"]
        try:
            price = cached_file_2["businesses"][x]["price"]
        except:
            price = "No price range available."
        review_num = cached_file_2["businesses"][x]["review_count"]
        name = cached_file_2["businesses"][x]["alias"]
        address = cached_file_2["businesses"][x]["location"]["display_address"]
        print('--------------------- Hotel ----------------------')
        print(name.replace('-', ' ').upper() + ' ' + str(address))
        print('Rating: ' + str(rating))
        print('Number of reviews: ' + str(review_num))
        print('Price range: ' + str(price))
        print('')
    return (name.replace('-', ' '), str(address), str(rating), str(review_num), str(price))

#SECOND USER PROMPT
user_inp_2 = input('To view restaurant and hotel reccomendations in this city, enter "view".\nTo exit the program, enter "exit": ')

if user_inp_2 == 'view':
    get_restaurants(user_inp)
    print(' ')
    get_hotels(user_inp)


elif user_inp_2 == 'exit':
    print ('\nThanks, and happy travels!')
    exit()

else:
    print('Please enter a valid command.')
    user_inp_2 = input('To view restaurant and hotel reccomendations in this city, enter "view".\nTo exit the program, enter "exit": ')


state_dict = {
        'ak': 'Alaska',
        'al': 'Alabama',
        'ar': 'Arkansas',
        'az': 'Arizona',
        'ca': 'California',
        'co': 'Colorado',
        'ct': 'Connecticut',
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
        'ms': 'Mississippi',
        'mt': 'Montana',
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
        'ri': 'Rhode Island',
        'sc': 'South Carolina',
        'sd': 'South Dakota',
        'tn': 'Tennessee',
        'tx': 'Texas',
        'ut': 'Utah',
        'va': 'Virginia',
        'vt': 'Vermont',
        'wa': 'Washington',
        'wi': 'Wisconsin',
        'wv': 'West Virginia',
        'wy': 'Wyoming'
}
#new netstate function to gather info from every state
def get_all_netstate(state):
    baseurl = 'http://www.netstate.com/states/alma/{}_alma.htm'.format(state)
    html = get_cached_netstate(baseurl)
    soup = BeautifulSoup(html, 'html.parser')
    container =soup.find(id='container')
    my_table = container.find('table')
    inner_table = my_table.find('table')
    tr = inner_table.find_all('tr')[0]
    td = tr.find_all('td')
    city = td[1].string
    population = td[2].string
    #print(city + ', ' + state.upper() + ': population of ' + population + '\n ')
    return (city, state, population)

def get_city_data():
    city_data_lst = []
    for x in state_dict.keys():
        state_info = get_all_netstate(x)
        city_data_lst.append(state_info)
    return city_data_lst

#new yelp function to gather info from every state
def get_all_restaurants(state):
    city = get_all_netstate(state)
    search_results = yelp_api.search_query(term = 'Restaurant',
    location = str(city) + ', ' + str(state.upper()))
    with open('yelp_cache.json', 'w') as CACHE_DICT:
        json.dump(search_results, CACHE_DICT)

    with open('yelp_cache.json') as json_data:
        cached_file = json.load(json_data)

    for x in range(0, 5):
        try:
            rating = cached_file["businesses"][x]["rating"]
        except:
            rating = "No rating available."
        try:
            price = cached_file["businesses"][x]["price"]
        except:
            price = "No price range available."
        review_num = cached_file["businesses"][x]["review_count"]
        name = cached_file["businesses"][x]["alias"]
        address = cached_file["businesses"][x]["location"]["display_address"]
    return (name.replace('-', ' '), str(address), str(rating), str(review_num), str(price))


def get_restaurant_data():
    restaurant_lst = []
    for x in state_dict.keys():
        restaurant_info = get_all_restaurants(x)
        restaurant_lst.append(restaurant_info)
    #print(restaurant_lst)
    return restaurant_lst


#CREATE DB WITH FOLLOWING TABLES:
#table 'NetState' - city (w/ID), state, population (50 of them)
#table 'YelpResults' - city (w/ID), category, price, rating, review #

DBNAME = 'netstate.db'

def init_db():
    conn = sqlite.connect(DBNAME)
    cur = conn.cursor()

    statement = '''
        DROP TABLE IF EXISTS 'NetState';
    '''
    cur.execute(statement)
    conn.commit()

    statement = '''
        DROP TABLE IF EXISTS 'YelpRestaurantResults';
    '''
    cur.execute(statement)
    conn.commit()

    statement = '''
        CREATE TABLE 'NetState' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'City' TEXT NOT NULL,
            'StateAbbr' TEXT NOT NULL,
            'Population' INTEGER NOT NULL

        );
    '''
    cur.execute(statement)
    conn.commit()

    statement = '''
        CREATE TABLE 'YelpRestaurantResults' (
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'RestaurantName' TEXT NOT NULL,
            'Address' TEXT NOT NULL,
            'Rating' TEXT NOT NULL,
            'Review #' TEXT NOT NULL,
            'Price' TEXT NOT NULL
        );
    '''

    cur.execute(statement)
    conn.commit()
    conn.close()

def populate_db():
    conn = sqlite.connect(DBNAME)
    cur = conn.cursor()

    f = open(NETSTATE_CACHE, 'r')
    contents = f.read()
    json_data = json.loads(contents)

    for x in get_city_data():
        city = x[0]
        stateabbr = x[1]
        population = x[2]

        insertion = (None, city, stateabbr, population)
        statement = 'INSERT INTO "NetState" '
        statement += 'VALUES (?, ?, ?, ?)'
        cur.execute(statement, insertion)

    conn.commit()
    conn.close()

def populate_db_2():
    conn = sqlite.connect(DBNAME)
    cur = conn.cursor()

    f = open('yelp_cache.json', 'r')
    contents = f.read()
    yelp_res_data = json.loads(contents)

    for x in get_restaurant_data():
        name = x[0]
        address = x[1]
        rating = x[2]
        reviews = x[3]
        price = x[4]

        insertion = (None, name, address, rating, reviews, price) # reviews)
        statement = 'INSERT INTO "YelpRestaurantResults"'
        statement += 'VALUES (?, ?, ?, ?, ?, ?)'
        cur.execute(statement, insertion)

    conn.commit()
    conn.close()

init_db()
populate_db()
populate_db_2()

#PLOTLY COMPARISONS
def create_plot_1():
    fref = open('netstate_cache.json', 'r')
    f_contents = fref.read()
    state_data = json.loads(f_contents)
    city_list = []
    pop_list = []
    for state in get_city_data():
        pop_list.append(state[2])
        city_list.append(state[0])
    p_1 = 'Most Populous Cities in Every State'
    trace0 = go.Scatter(x = city_list, y = pop_list, mode = 'markers')
    data = go.Data([trace0])
    layout = dict(title = p_1, yaxis = dict(zeroline = False), xaxis = dict(zeroline = False))
    fig = dict(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Plot1')

def create_plot_2():
    fref = open('yelp_cache.json', 'r')
    f_contents = fref.read()
    yelp_data = json.loads(f_contents)
    name_list = []
    rev_list = []
    for r in get_restaurant_data():
        name_list.append(r[0])
        rev_list.append(r[3])
    p_2 = 'Number of Yelp Reviews of the Top Restaurant in Each Highest-Populated City'
    trace0 = go.Scatter(x = name_list, y = rev_list, mode = 'markers')
    data = go.Data([trace0])
    layout = dict(title = p_2, yaxis = dict(zeroline = False), xaxis = dict(zeroline = False))
    fig = dict(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Plot2')

def create_plot_3():
    fref = open('yelp_cache.json', 'r')
    f_contents = fref.read()
    yelp_data = json.loads(f_contents)
    name_list = []
    rating_list = []
    for r in get_restaurant_data():
        name_list.append(r[0])
        rating_list.append(r[2])
    p_3 = 'Yelp Rating Comparison of the Top Restaurant in Each Highest-Populated City'
    trace0 = go.Scatter(x = name_list, y = rating_list, mode = 'markers')
    data = go.Data([trace0])
    layout = dict(title = p_3, yaxis = dict(zeroline = False), xaxis = dict(zeroline = False))
    fig = dict(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Plot3')

def create_plot_4():
    fref = open('yelp_cache.json', 'r')
    f_contents = fref.read()
    yelp_data = json.loads(f_contents)
    name_list = []
    pr_list = []
    for r in get_restaurant_data():
        name_list.append(r[0])
        pr_list.append(r[4])
    p_4 = 'Yelp Price Range Comparison of the Top Restaurant in Each Highest-Populated City'
    trace0 = go.Scatter(x = name_list, y = pr_list, mode = 'markers')
    data = go.Data([trace0])
    layout = dict(title = p_4, yaxis = dict(zeroline = False), xaxis = dict(zeroline = False))
    fig = dict(data=data, layout=layout)
    plot_url = py.plot(fig, filename='Plot4')

user_inp_3 = input('To further view graph comparisons of cities along with their top restaurants, enter "view".\nOtherwise, enter "exit": ')

if user_inp_3 == 'view':
    create_plot_1()
    create_plot_2()
    create_plot_3()
    create_plot_4()
    print("Thank you, and happy travels!")
else:
    exit()
