# nyu-python-project
for use with NYU Stern Intro to python class

# Setup
# create a sam.gov account
# Navigate to: https://open.gsa.gov/api/get-opportunities-public-api/#user-account-api-key-creation and follow these steps to get an API Key
# this api key is good for 90 days from activation


```sh
#Create virtual environment
conda create -n prj-env python=3.11


#Activate the environment:
conda activate prj-env


#Install packages:

#pip install requests
#pip install plotly
#pip install python-dotenv

# best practice to list the packages in the requirements.txt file:
pip install -r requirements.txt



#Obtain an [API Key](https://www.alphavantage.co/support/#api-key) from Alphavantage. Then create a ".env" file in the root directory of the repo, and paste some contents in like this, but using your own api key:


# this is the ".env" file:

SAM_API_KEY="__________"


## Usage

#Run the script:

python -m api/data_pull.py
'''