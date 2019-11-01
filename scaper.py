from craigslist import CraigslistHousing
from pprint import pprint
cl = CraigslistHousing(site='sfbay', area='sfc', category='apa', filters={'max_price': 3500, 'min_price': 2000})
results = cl.get_results(sort_by='newest', geotagged=True, limit=20)
for result in results:
    pprint(result)
