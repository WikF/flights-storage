import logging
from psycopg2.extras import LoggingConnection

import psycopg2
import requests

latitude = "35.0497"
longitude = "-89.9789"

API_KEY = "UUY9J867T5PDBGGY7QX4UZ9ND"
BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("loggerinformation")
ml_db = psycopg2.connect("postgres://postgres@localhost:5433/pgml_development")


def return_data_for_weather_hist_api(limit=10, flight_id=None):
    if not flight_id:
        with ml_db.cursor() as curs:
            curs.execute(f"select * from public.data_to_fetch_weather limit {limit}")
            return curs.fetchall()
    with ml_db.cursor() as curs:
        curs.execute(f"select * from public.data_to_fetch_weather where flight_id='{flight_id}' limit {limit}")
        return curs.fetchall()

def all_existing_records():
    with ml_db.cursor() as curs:
        curs.execute(f"""
        select distinct lat, lon, datetime
        from weather_hist
""")
        return curs.fetchall()


def records_for_flight_id(flight_id):
    with ml_db.cursor() as curs:
        curs.execute(f"""
        select distinct lat, lon, datetime
        from weather_hist
""")
        return curs.fetchall()


def save_weather_data_to_db(flight_id=None, limit=900):
    flights = return_data_for_weather_hist_api(limit=limit, flight_id=flight_id)
    weather_reports = [i for i in all_existing_records()]

    if flight_id:
        weather_reports = [i for i in records_for_flight_id(flight_id)]
    for flight in flights:
        if (flight[1], flight[2], flight[3].date().isoformat()) not in weather_reports:
            LAT = flight[1]
            LON = flight[2]
            DATETIME = flight[3].isoformat()[:-7]
            api_result = requests.get(
                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{LAT},{LON}/{DATETIME}?unitGroup=metric&key={API_KEY}&include=current")
            print(api_result.text)
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

            with ml_db.cursor() as curs:
                curs.execute(f"""INSERT INTO public.weather_hist(
                lat, lon, temp, feelslike, humidity, dew, precip, precipprob, snow, snowdepth, preciptype, windgust, windspeed, winddir, pressure,
visibility, cloudcover, solarradiation, solarenergy, uvindex, conditions, datetime)
                VALUES ('{lat}', '{lon}', '{temp}', '{feelslike}', '{humidity}', '{dew}', '{precip}', '{precipprob}', '{snow}', '{snowdepth}', '{preciptype}', '{windgust}', '{windspeed}', '{winddir}','{pressure}', '{visibility}', '{cloudcover}', '{solarradiation}', '{solarenergy}', '{uvindex}', '{conditions}', '{timestamp}');
            """)

