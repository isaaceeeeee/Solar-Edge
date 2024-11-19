# Site Details 
import requests
import pandas as pd
import json

api_key = "TJ4FD471UHFDHH2134D3X3SPI3FHP2RG"
site = 1337258
base_url = f"https://monitoringapi.solaredge.com/site/{site}/details"
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

"""
Example Data (JSON): 

{
    "details": {
        "id": 1,
        "name": "Name",
        "accountId": 1,
        "status": "Active",
        "peakPower": 100.0,
        "lastUpdateTime": "2024-01-01",
        "installationDate": "2024-01-01",
        "ptoDate": null,
        "notes": null,
        "type": "Optimizers & Inverters",
        "location": {
            "country": "United Kingdom",
            "city": "City",
            "address": "Address",
            "zip": "Post Code",
            "timeZone": "Europe/London",
            "countryCode": "GB"
        },
        "alertQuantity": 0,
        "highestImpact": 0,
        "primaryModule": {
            "manufacturerName": "Manufacturer",
            "modelName": "Name",
            "maximumPower": 100.0,
            "temperatureCoef": -0.00
        },
        "uris": {
            "DETAILS": "/site/1/details",
            "DATA_PERIOD": "/site/1/dataPeriod",
            "OVERVIEW": "/site/1/overview"
        },
        "publicSettings": {
            "isPublic": false
        }
    }
}
  
"""
