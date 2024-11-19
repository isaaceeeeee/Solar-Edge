# Data Period 
import requests
import pandas as pd
import json

api_key = "TJ4FD471UHFDHH2134D3X3SPI3FHP2RG"
site = 1337258
base_url = f"https://monitoringapi.solaredge.com/site/{site}/dataPeriod"
params = {
    'size': 100,
    # 'searchText': '', # Any unique search criteria
    'sortProperty': 'name',
    'sortOrder': 'ASC',
    # 'timeUnit': 'DAY',
    # 'startDate': '2024-07-01',
    # 'endDate': '2024-09-30',
    'api_key': api_key
}
response = requests.get(base_url, params=params)
function = pd.DataFrame(response)
function = response.json()
print(json.dumps(function, indent=4))
with open("output.json", "w") as json_file:
    json.dump(function, json_file, indent=4)

'''

Example Data (JSON):
{
    "dataPeriod": {
        "startDate": "2019-11-06",
        "endDate": "2024-11-19"
    }
}

'''
