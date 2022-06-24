import json
import requests

from create_tables import db

latitude = "35.0497"
longitude = "-89.9789"

API_KEY = "852BXS8K3HW8XPM7429JEDSKQ"
BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'


def return_data_for_weather_hist_api(limit=10):
    flights = db.prepare(f"select * from data_to_fetch_weather_hist limit {limit}")
    return flights


def all_existing_records():
    records = db.prepare(f"""
        select distinct lat, lon, datetime
        from weather_hist
""")
    return records


def save_weather_data_to_db(limit=10):
    flights = return_data_for_weather_hist_api(limit)
    weather_reports = [i for i in all_existing_records()]
    for flight in flights():
        if (flight[0], flight[1], flight[2].date().isoformat()) not in weather_reports:
            LAT = flight[0]
            LON = flight[1]
            DATETIME = flight[2].isoformat()
            api_result = requests.get(
                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{LAT},{LON}/{DATETIME}?unitGroup=metric&key={API_KEY}&include=current")
            print(api_result.json().get("currentConditions"))
            result = api_result.json()
            date = result.get("days")[0].get("datetime")
            time = result.get("currentConditions").get("datetime")
            timestamp= date+" "+time
            lat = result.get("latitude")
            lon = result.get("longitude")
            temp = result.get("currentConditions").get("temp")
            feelslike = result.get("currentConditions").get("feelslike")
            humidity = result.get("currentConditions").get("humidity")
            dew = result.get("currentConditions").get("dew")
            precip = result.get("currentConditions").get("precip")
            precipprob = result.get("currentConditions").get("precipprob")
            snow = result.get("currentConditions").get("snow")
            snowdepth = result.get("currentConditions").get("snowdepth")
            try:
                preciptype = result.get("currentConditions").get("preciptype")[0]
            except Exception:
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


            db.execute(f"""INSERT INTO public.weather_hist(
                lat, lon, temp, feelslike, humidity, dew, precip, precipprob, snow, snowdepth, preciptype, windgust, windspeed, winddir, pressure,
visibility, cloudcover, solarradiation, solarenergy, uvindex, conditions, datetime)
                VALUES ('{lat}', '{lon}', '{temp}', '{feelslike}', '{humidity}', '{dew}', '{precip}', '{precipprob}', '{snow}', '{snowdepth}', '{preciptype}', '{windgust}', '{windspeed}', '{winddir}','{pressure}', '{visibility}', '{cloudcover}', '{solarradiation}', '{solarenergy}', '{uvindex}', '{conditions}', '{timestamp}');
            """)


save_weather_data_to_db(150)

