import json
import requests

from create_tables import db

TOKEN = "1f5211c58e56c158ff8991bf8c3d417b"

params = {
    'access_key': TOKEN,
    'limit': '1',
}

API_KEY="86b4c54cb16944898969c6d9d0b9a20d"

api_result = requests.get(f"https://api.weatherbit.io/v2.0/history/daily?start_date=2022-06-06&end_date=2022-06-07&city=Fairbanks&key={API_KEY}")
api_response = api_result.json()
with open('weather.json', 'w') as f:
    json.dump(api_response, f)


def return_data_for_weather_hist_api(limit=10):
    flights = db.prepare(f"select * from data_to_fetch_weather_hist limit {limit}")
    return flights


def all_existing_records():
    records = db.prepare(f"""
        select distinct lat, lon, datetime
        from weather_conditions
""")
    return records


def save_weather_data_to_db(limit=10):
    flights = return_data_for_weather_hist_api(limit)
    weather_reports  = [i for i in all_existing_records()]
    for flight in flights():
        if (flight[0], flight[1], flight[2].date().isoformat()) not in weather_reports:
            LAT = flight[0]
            LON = flight[1]
            START_DATETIME = flight[2].isoformat()
            api_result = requests.get(
        f"https://api.weatherbit.io/v2.0/history/daily?start_date={START_DATETIME}&end_date={END_DATETIME}&lat={LAT}&lon={LON}&key={BIT_API_KEY}")
            result = api_result.json()
            date = result.get("days").get("datetime")
            time = result.get("currentConditions").get("datetime")
            timestamp= date+" "+time
            lat = result.get("lat")
            lon = result.get("lon")
            temp = result.get("currentConditions").get("temp")
            feelslike = result.get("currentConditions").get("feelslike")
            humidity = result.get("currentConditions").get("humidity")
            dew = result.get("currentConditions").get("dew")
            precip = result.get("currentConditions").get("precip")
            precipprob = result.get("currentConditions").get("precipprob")
            snow = result.get("currentConditions").get("snow")
            snowdepth = result.get("currentConditions").get("snowdepth")
            preciptype = result.get("currentConditions").get("preciptype")
            windgust = result.get("currentConditions").get("windgust")
            windspeed = result.get("currentConditions").get("windspeed")
            winddir = result.get("currentConditions").get("winddir")
            pressure = result.get("currentConditions").get("pressure")
            visibility = result.get("currentConditions").get("visibility")
            cloudcover = result.get("currentConditions").get("cloudcover")
            solarradiation = result.get("currentConditions").get("solarradiation")
            solarenergy = result.get("currentConditions").get("solarenergy")
            uvindex = result.get("currentConditions").get("uvindex")
            conditions = result.get("currentConditions").get("conditions")


            db.execute(f"""INSERT INTO public.weather_conditions(
                lat, lon,, temp, feelslike, humidity, dew, precip, precipprob, snow, snowdepth, preciptype, windgust, windspeed, winddir, pressure,
visibility, cloudcover, solarradiation, solarenergy, uvindex, conditions, datetime)
                VALUES ('{lat}', '{lon}', '{temp}', '{feelslike}', {humidity}, '{dew}', '{precip}', '{precipprob}', 
                '{snow}', '{snowdepth}', '{preciptype}', '{windgust}', '{windspeed}', '{winddir}','{pressure}', '{visibility}', '{cloudcover}', '{solarradiation}', '{solarenergy}', '{uvindex}', '{conditions}', '{timestamp}');
            """)

save_weather_data_to_db(800)