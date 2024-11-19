Solar-Edge Integration Tools

This repository contains Python scripts for interacting with SolarEdge's Monitoring API. It enables automation and data extraction for energy and power management across multiple sites, providing detailed insights into solar production and consumption.

Features

Power Details API: Fetch 15-minute resolution data for site production and consumption.
Bulk Energy API: Retrieve daily energy data for multiple sites within a specified range.
Data Transformation: Converts JSON responses into structured CSV or DataFrame formats for analysis.

Installation

Clone this repository:
bash
Copy code
git clone https://github.com/isaaceeeeee/Solar-Edge.git  
Install dependencies:
bash
Copy code
pip install -r requirements.txt  
Configuration

Update the config.json file with your API key and necessary parameters:

json
Copy code
{  
  "api_key": "your_api_key"  
}  
Usage

Power Details API

Fetch power data for a single site:

bash
Copy code
python power_details.py  
Bulk Energy API

Retrieve bulk energy data for multiple sites:


bash
Copy code
python bulk_energy.py  

Output

The scripts output JSON and CSV files containing structured energy or power data for the specified sites and date ranges.

Contributions

Contributions are welcome! Please submit an issue or a pull request to propose changes or suggest features.

License

MIT License

