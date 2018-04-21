# For my final project, I decided to focus in on a topic which has been extremely relevant to me throughout the entirety of my life. I was raised in an international household, both parents having immigrated to the United States. Due to the nature of their life trajectory in terms of relocating their lives to this country, they are both gigantic advocates of travelling and more largely, seeing the world. Travelling, more specifically the United States, has been a priority for my family ever since they arrived here; my parents are determined to see what each state has to offer, and we have sporadically travelled to many unfamiliar states around the nation. For these states, my family heavily relies on the use of Yelp to direct our destination, restaurant, and lodging decisions during our trips. I want to create an interactive search engine that will ultimately help travelers in the United States find popular cities in the United States that they desire to visit, as well as provide them with information on different options of where to eat and where to stay in those specified locations.
# Firstly, I will crawl and scrape multiple pages from a site titled netstate.com, which provides information on the 50 states and the cities within them (and will give me approximately 8 challenge points). Once a state is selected - a state abbreviation is typed into the command line – it will access a category on the website available, titled “Ten largest cities by population”, in which recent U.S Census data is used to fill in the most populous cities in each state. My search engine will crawl the site and collect the data for the most populous city in each of the 50 states. It will also aggregate the data of each state, city, and its population into a database. The program will allow the user to input any state name and in return receive an output of that state’s most populated city and what that population is.
#
# 	An output example of this first search could look like:
#
#  	 Little Rock, AR: population of 183,133
#
# The search engine user will then be able to deeper investigate the city that resulted in their search and gain greater knowledge of the food and lodging amenities present there. For this I will utilize, Yelp Fusion, which is a Web API we haven’t used prior that requires an API key and provides a challenge score of 4 points. There are two categories that I will be accessing, “Hotels” and “Restaurants”. The search engine will return a list of the top 5 best hotels and restaurants in that city. There will also be information in each of the results which will show the location price point ($, $$, $$$, or $$$$), the number of reviews, and the rating of each of the 5 hotels or restaurants in the resulting list after the user searches. The top 5 hotels and restaurants, along with their city, will also be stored in in a database (my second).
#
#
#
# In summation:
# 1.	The data sources you intend to use, along with your self-assessment of the “challenge score” represented by your data source selection:
# •	Crawling/scraping multiple pages of a new site: Net State (8 challenge points) http://www.netstate.com/state_cities.htm
# •	API doc I have never used w/API key or HTTP authorization: Yelp Fusion (4 challenge points) https://www.yelp.com/developers/documentation/v3
#
# 2.	The presentation options you plan to support (what information will be displayed):
# •	Most populous city in selected state (along with numerical population)
# •	Top 5 hotel/travel search results in selected city
# •	Top 5 restaurants search results in selected city
#
# 3.	The presentation tool(s) you plan to use:
# •	Ploty graph visual option of both of the top 5 lists, graphed with their price points or with the number of reviews they received.
#
# 
