import json
import requests


API_KEY="86b4c54cb16944898969c6d9d0b9a20d"

api_result = requests.get(f"https://api.weatherbit.io/v2.0/history/daily?start_date=2022-06-06&end_date=2022-06-07&city=Fairbanks&key={API_KEY}")
api_response = api_result.json()
with open('weather.json', 'w') as f:
    json.dump(api_response, f)

