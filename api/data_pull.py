naics_code_list = [541519, 334111, 513210, 541512, 423430]

import os
import json
import requests
import webbrowser
from dotenv import load_dotenv


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

# Load data from my_dict.json
with open("my_dict.json", "r") as file:
    opps = json.load(file)

print(opps.keys())
print(len(opps['opportunitiesData']))
print(type(opps['opportunitiesData'][0]))
print(opps['opportunitiesData'][0].keys())
print('-------------------------')
print('Select data from the first opportunity in the list:')
title = opps['opportunitiesData'][0]['title']
posted_date = opps['opportunitiesData'][0]['postedDate']
type_of_opportunity = opps['opportunitiesData'][0]['type']
set_aside = opps['opportunitiesData'][0]['typeOfSetAside']
amount = opps['opportunitiesData'][0]['award']['amount']
contact_info = opps['opportunitiesData'][0]['pointOfContact'][0]

print('Title: ' + title)
print('Posted on: ' + posted_date)
print('Type: ' + type_of_opportunity)
print('Set Aside: ' + set_aside)
print('Amount: ' + amount)
print(contact_info)
print('Contact Inf:')
contact_name = contact_info['fullName']
contact_phone = contact_info['phone']
contact_email = contact_info['email']
print(contact_name)
print(contact_phone)
print(contact_email)

# Generate the HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Opportunity Details</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
        }}
        .opportunity {{
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 8px;
            max-width: 600px;
            margin: 0 auto;
        }}
        .opportunity h2 {{
            font-size: 24px;
            margin-bottom: 10px;
        }}
        .opportunity p {{
            margin: 5px 0;
        }}
        .contact-info {{
            margin-top: 20px;
            padding: 10px;
            border-top: 1px solid #ccc;
        }}
        .contact-info h3 {{
            margin-top: 0;
        }}
    </style>
</head>
<body>
    <div class="opportunity">
        <h2>Title: {title}</h2>
        <p><strong>Posted on:</strong> {posted_date}</p>
        <p><strong>Type:</strong> {type_of_opportunity}</p>
        <p><strong>Amount:</strong> ${amount}</p>
        <div class="contact-info">
            <h3>Contact Information</h3>
            <p><strong>Name:</strong> {contact_name}</p>
            <p><strong>Phone:</strong> {contact_phone}</p>
            <p><strong>Email:</strong> <a href="mailto:{contact_email}">{contact_email}</a></p>
        </div>
    </div>
</body>
</html>
"""

# Save the HTML content to a file
html_file = "opportunity_details.html"
with open(html_file, "w") as file:
    file.write(html_content)

print("HTML content has been written to opportunity_details.html")

# Automatically open the HTML file in a web browser
webbrowser.open(f'file://{os.path.realpath(html_file)}')