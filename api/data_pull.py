naics_code_list = [541519, 334111, 513210, 541512, 423430]

# import secrets
api_key = os.getenv("SAM_API_KEY", default="demo")

import requests

# max limit = 1000
sam_url = f'https://api.sam.gov/prod/opportunities/v2/search?limit=1000&api_key={api_key}&postedFrom=08/05/2024&postedTo=08/06/2024&ptype=a&ncode=541519'


opportunities = requests.get(sam_url).json()

print(type(opportunities))
print(opportunities.keys())
print(len(opportunities['opportunitiesData']))

opportunities['opportunitiesData'][0]