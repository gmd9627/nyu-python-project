# nyu-python-project
for use with NYU Stern Intro to python class

* # Setup
# create a sam.gov account
# Navigate to: https://open.gsa.gov/api/get-opportunities-public-api/#user-account-api-key-creation and follow these steps to get an API Key
# this api key is good for 90 days from activation
# Then create a ".env" file in the root directory of the repo, and paste some contents in like this, but using your own api key:

# SAM_API_KEY="__________"*




```sh
#Create virtual environment
conda create -n prj-env python=3.11


#Activate the environment:
conda activate prj-env


# Install libraries via the requirements.txt file:
pip install -r requirements.txt


## Usage

#Run the script:

python -m api/data_pull.py
'''