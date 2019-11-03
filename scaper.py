from craigslist import CraigslistHousing
import search_settings as ss
import os
from pprint import pprint
import string

if os.path.exists('search_results.html'):
    os.remove('search_results.html')
cl = CraigslistHousing(site='sfbay', area=ss.CRAIGSLIST_SUB, category='apa', filters={'max_price': 3500, 'min_price': 2000})
results = cl.get_results(sort_by='newest', geotagged=True, limit=20)
href = "<a href="
href2 = "\>"
href3 = "</a>"
for result in results:
  
    #pprint(href + result["url"] + href2 + "holder" + '</a>', depth=1, width=100)
    #print(result['url'])
    
    search_results = open('search_results.html', 'a+')
    
    
    print(href + result["url"] + href2 + "holder" + href3, file = search_results)
    search_results = str(search_results)
    print(type(search_results))
    search_results = search_results.rstrip('/')
    
    #search_results.close()
# for result in results:
    #pprint(result['url'], depth=1, width=100)
    #search_results = open('search_results.html', 'a+')     
    #print('<a href="{result['url']}"file=search_results)
    #print(result['url'], file=search_results)
    #search_results.close()
print("<a href=")
print(href)
