naics_code_list = [541519, 334111, 513210, 541512, 423430]

import os
from dotenv import load_dotenv
import requests
import json


load_dotenv()


# import secrets
api_key = os.getenv("SAM_API_KEY", default="demo")


# max limit = 1000
sam_url = f'https://api.sam.gov/prod/opportunities/v2/search?limit=1000&api_key={api_key}&postedFrom=08/05/2024&postedTo=08/06/2024&ptype=a&ncode=541519'


opportunities = requests.get(sam_url).json()

print(type(opportunities))
print(opportunities.keys())
print(len(opportunities['opportunitiesData']))

opportunities['opportunitiesData'][0]

with open("my_dict.json", "r") as file:
    opps = json.load(file)

    # now, reference the file and pull some data from the first opportinity:

print(opps.keys())
print(len(opps['opportunitiesData']))
print(type(opps['opportunitiesData'][0]))
print(opps['opportunitiesData'][0].keys())
print('-------------------------')
print('Select data from the first opportunity in the list:')
print('Title: ' + (opps['opportunitiesData'][0]['title']))
print('Posted on: ' + (opps['opportunitiesData'][0]['postedDate']))
print('Type: ' + (opps['opportunitiesData'][0]['type']))
print('Set Aside: ' + (opps['opportunitiesData'][0]['typeOfSetAside']))
print('Amount: ' + (opps['opportunitiesData'][0]['award']['amount']))
print((opps['opportunitiesData'][0]['pointOfContact']))
print('Contact Inf:')
print((opps['opportunitiesData'][0]['pointOfContact'][0]['fullName']))
print((opps['opportunitiesData'][0]['pointOfContact'][0]['phone']))
print((opps['opportunitiesData'][0]['pointOfContact'][0]['email']))