# solaredge.py
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
