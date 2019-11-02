# setting for the craigslist search

import os

# minimum price
MIN_PRICE = 2000

# maximum price
MAX_PRICE = 3500

# craigslist site to search
# this case I want to search the sfbay site
CRAIGSLIST_SITE = 'sfbay'

# craigslist sub to search
# this case I want to search the peninsula subdirectory
CRAIGSLIST_SUB = 'pen'

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "redwood_city": [
        [37.409339, -122.335912],
        [37.562461,	-122.140858],
    ],
    "san_mateo": [
        [37.409339, -122.446209],
        [37.65479, -122.23692],
    ]
}

