from craigslist import CraigslistHousing
import search_settings as ss
import os
#from pprint import pprint
import string
import smtplib
from email.message import EmailMessage
#import test_email


# -- TODO --
#  convert results to list    !!!!!!!!!done
#  no need for text file
#  make email a class and pass list to it.
#  insert list into html and send


if os.path.exists('search_results.txt'):
    os.remove('search_results.txt')
cl = CraigslistHousing(site='sfbay', area=ss.CRAIGSLIST_SUB, category='apa', filters={'max_price': 3000, 'min_price': 2000})

results = []
results = cl.get_results(sort_by='newest', geotagged=True, limit=20)

print(type(results))
lineList = list()
    
#for result in results:
#    search_results = open('search_results.txt', 'a+')
#    search_results.write(result["url"] + "\n")
    
#lineList = [line.rstrip('\n') for line in open('search_results.txt')]

for result in results:
    lineList.append(result["url"])
    
print(type(lineList))

for line in lineList:
    
    print(line)
