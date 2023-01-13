import datetime
from time import sleep

import requests
from utils import insert_flight_data_to_db
from weather_utils import save_weather_data_to_db


def flights(days: int):
    base = datetime.date.today()

    starts = [base - datetime.timedelta(days=x) for x in range(1, days)]
    ends = [base - datetime.timedelta(days=x) for x in range(days-1)]
    count=0
    for start, end in zip(starts, ends):
        count +=1
        print(start, end)
        date = f"startRange={start}T00:00:00Z&endRange={end}T00:00:00Z"
        response = requests.get(f'https://api.airfranceklm.com/opendata/flightstatus?{date}',
                                headers={'Api-Key': 'dqfp7ndxaq7srkvaqt8w6nec'})
        print(response.status_code)
        api_response = response.json()

        print(api_response["operationalFlights"])

        insert_flight_data_to_db(api_response)
        if count == 999:
            break


def flight_details_to_predict_to_db(flight_id: str):
    response = requests.get(f'https://api.airfranceklm.com/opendata/flightstatus/{flight_id}',
                                headers={'Api-Key': 'dqfp7ndxaq7srkvaqt8w6nec'})
    print(response.status_code)
    api_response = response.json()
    insert_flight_data_to_db(api_response, 'flights')
    print('to db inserted now weather')
    sleep(1)
    save_weather_data_to_db(flight_id=flight_id)
    print('to weather inserted done')
    return api_response


def provide_data_for_model(flight_id):
    query = f"""SELECT
    flight_id,
      (select airline_category from data_prepared where airline = airline) as airline_category,
      CAST(number_of_legs AS FLOAT4),
      (select airline_category from data_prepared where flight_status=flight_status) as flight_status_category,
      CAST(arrival_longitude AS FLOAT4),
      CAST(arrival_lattitude AS FLOAT4),
      (select airline_category from data_prepared where arrival_airport_name=arrival_airport_name)
          as arrival_airport_name_category,
      CAST(EXTRACT( MONTH FROM CAST(ARRIVAL_DATETIME AS TIMESTAMP)) AS FLOAT4) AS ARRIVAL_MONTH,
      CAST(EXTRACT(DOW FROM CAST(ARRIVAL_DATETIME AS TIMESTAMP)) AS FLOAT4) AS ARRIVAL_DOW,
      CAST(EXTRACT(DOW FROM CAST(ARRIVAL_DATETIME AS TIMESTAMP)) AS FLOAT4) AS ARRIVAL_WEEK,
      CAST(departure_longitude AS FLOAT4),
      CAST(departure_lattitude AS FLOAT4),
      (select airline_category from data_prepared where departure_airport_name=departure_airport_name)
          as departure_airport_name_category,
      CAST(EXTRACT(MONTH FROM CAST(DEPARTURE_DATETIME AS TIMESTAMP)) AS FLOAT4) DEPARTURE_MONTH,
      CAST(EXTRACT(DOW FROM CAST(DEPARTURE_DATETIME AS TIMESTAMP)) AS FLOAT4) AS DEPARTURE_DOW,
      CAST(EXTRACT(week FROM CAST(DEPARTURE_DATETIME AS TIMESTAMP)) AS FLOAT4) AS DEPARTURE_WEEK,

      (select airline_category from data_prepared where visibility=visibility) as visibility_category,
      (select airline_category from data_prepared where winddir=winddir) as winddir_category,
      (select airline_category from data_prepared where conditions=conditions) as conditions_category,
      (select airline_category from data_prepared where windspeed=windspeed) as windspeed_category,
      (select airline_category from data_prepared where precip=precip) as precip_category,
      (select airline_category from data_prepared where temp=temp) as temp_category
    FROM flights
    JOIN weather_hist
    on((flights.arrival_longitude = lon and flights.arrival_lattitude = lat and to_char(timestamptz(arrival_datetime),
       'yyyy-mm-dd') = left(datetime, 10))
    or (flights.departure_longitude=lon and flights.departure_lattitude=lat and to_char(timestamptz(departure_datetime), 'yyyy-mm-dd')=left(
        datetime, 10)))
   WHERE flight_id={flight_id};"""

