# Site Power
import requests
import pandas as pd
import json

# API Configuration
api_key = "TJ4FD471UHFDHH2134D3X3SPI3FHP2RG"
site_id = 1337258
base_url = f"https://monitoringapi.solaredge.com/site/{site_id}/powerDetails"

# Request parameters
params = {
    'meters': 'PRODUCTION,CONSUMPTION',
    'timeUnit': 'QUARTER_OF_AN_HOUR',  
    'startTime': '2024-07-01 00:00:00',
    'endTime': '2024-07-31 23:59:59',
    'api_key': api_key
}
response = requests.get(base_url, params=params)
if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=4))
    with open("output.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

    if 'powerDetails' in data and 'meters' in data['powerDetails']:
        meter_data = []
        for meter in data['powerDetails']['meters']:
            meter_type = meter['type']
            for value in meter['values']:
                meter_data.append({
                    'meter_type': meter_type,
                    'date': value['date'],
                    'power_value': value.get('value', 0)
                })
        df = pd.DataFrame(meter_data)
        print(df.head())
