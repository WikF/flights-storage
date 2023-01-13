import json
import requests


API_KEY="xxx"

api_result = requests.get(f"https://api.weatherbit.io/v2.0/history/daily?start_date=2022-06-06&end_date=2022-06-07&city=Fairbanks&key={API_KEY}")
api_response = api_result.json()
with open('weather.json', 'w') as f:
    json.dump(api_response, f)

