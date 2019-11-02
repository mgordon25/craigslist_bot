from craigslist import CraigslistHousing
import search_settings as ss

from pprint import pprint
cl = CraigslistHousing(site='sfbay', area=ss.CRAIGSLIST_SUB, category='apa', filters={'max_price': 3500, 'min_price': 2000})
results = cl.get_results(sort_by='newest', geotagged=True, limit=20)
for result in results:
    #pprint(result, depth=1, width=100)
    search_results = open('search_results.txt', 'a+')     
    print(result['url'], file=search_results)
    search_results.close()
