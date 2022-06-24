import datetime

import requests

import json

start_range="2022-06-04"
end_range="2022-06-05"
# print(response.status_code)
# api_response = response.json()
base = datetime.date.today()
base = datetime.date(year=2022, month=3, day=10)

starts = [base - datetime.timedelta(days=x) for x in range(1, 121)]
ends = [base - datetime.timedelta(days=x) for x in range(120)]


for start, end in zip(starts, ends):
    print(start, end)
    date = f"startRange={start}T00:00:00Z&endRange={end}T00:00:00Z"
    response = requests.get(f'https://api.airfranceklm.com/opendata/flightstatus?{date}',
                            headers={'Api-Key': 'y796h8b5rxy9yw5tzmxhwp5h'})
    print(response.status_code)
    api_response = response.json()
    with open(f'jsons/klm_flights_{start}-{datetime.date.today()}.json', 'w') as f:
         json.dump(api_response, f)

print('done')

