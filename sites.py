# sites.py
# Creates a list of all sites registered under your account
import requests
import pandas as pd
import json

api_key = "API_KEY"
function = "sites"
request = "list"
base_url = f"https://monitoringapi.solaredge.com/{function}/{request}"
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
Example output (JSON):
{
    "sites": {
        "count": 1,
        "site": [
            {
                "id": 1,
                "name": "Site Name",
                "accountId": 1,
                "status": "Active",
                "peakPower": 100.0,
                "lastUpdateTime": "2024-01-01",
                "installationDate": "2024-01-01",
                "ptoDate": null,
                "notes": "",
                "type": "Optimizers & Inverters",
                "location": {
                    "country": "United Kingdom",
                    "city": "City",
                    "address": "Address",
                    "address2": "",
                    "zip": "Post Code",
                    "timeZone": "Europe/London",
                    "countryCode": "GB"
                },
                "alertQuantity": 1,
                "highestImpact": 2,
                "primaryModule": {
                    "manufacturerName": "Manufacturer",
                    "modelName": "Model",
                    "maximumPower": 100.0
                },
                "uris": {
                    "DETAILS": "/site/1/details",
                    "DATA_PERIOD": "/site/1/dataPeriod",
                    "OVERVIEW": "/site/1/overview"
                },
                "publicSettings": {
                    "isPublic": false
                }
            },
        ]
    }
}
'''
