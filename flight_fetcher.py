#!/usr/bin/env python3

import json
import requests

TOKEN = "1f5211c58e56c158ff8991bf8c3d417b"

params = {
    'access_key': TOKEN,
    'limit': '1',
}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()
with open('mydata.json', 'w') as f:
    json.dump(api_response, f)

