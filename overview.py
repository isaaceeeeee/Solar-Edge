# Site Overview 
import requests
import pandas as pd
import json

api_key = "API_KEY"
site = 1337258
base_url = f"https://monitoringapi.solaredge.com/site/{site}/overview"
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
    "overview": {
        "lastUpdateTime": "2024-01-01 00:00:00",
        "lifeTimeData": {
            "energy": 100.0
        },
        "lastYearData": {
            "energy": 100.0
        },
        "lastMonthData": {
            "energy": 100.0
        },
        "lastDayData": {
            "energy": 100.0
        },
        "currentPower": {
            "power": 100.0
        },
        "measuredBy": "METER"
    }
}

'''
