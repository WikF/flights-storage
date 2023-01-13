import datetime

import requests

from db_utils.create_tables import db

BIT_API_KEY="319d5773811d48fda3d5816c308e4787"


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
            START_DATETIME: datetime.date = flight[2].date()
            END_DATETIME=START_DATETIME+datetime.timedelta(days=1)
            api_result = requests.get(
        f"https://api.weatherbit.io/v2.0/history/daily?start_date={START_DATETIME}&end_date={END_DATETIME}&lat={LAT}&lon={LON}&key={BIT_API_KEY}")
            result = api_result.json()
            print(result)
            city_name = result.get("city_name")
            lat = result.get("lat")
            lon = result.get("lon")
            rh = result.get("data")[0].get("rh")
            ax_wind_spd_ts = result.get("data")[0].get("max_wind_spd_ts")
            t_ghi = result.get("data")[0].get("t_ghi")
            max_wind_spd = result.get("data")[0].get("max_wind_spd")
            solar_rad = result.get("data")[0].get("solar_rad")
            wind_gust_spd = result.get("data")[0].get("wind_gust_spd")
            max_temp_ts = result.get("data")[0].get("max_temp_ts")
            min_temp_ts = result.get("data")[0].get("min_temp_ts")
            clouds = result.get("data")[0].get("clouds")
            max_dni = result.get("data")[0].get("max_dni")
            precip_gpm = result.get("data")[0].get("precip_gpm")
            wind_spd = result.get("data")[0].get("wind_spd")
            slp = result.get("data")[0].get("slp")
            ts = result.get("data")[0].get("ts")
            max_ghi = result.get("data")[0].get("max_ghi")
            temp = result.get("data")[0].get("temp")
            pres = result.get("data")[0].get("pres")
            dni = result.get("data")[0].get("dni")
            dewpt = result.get("data")[0].get("dewpt")
            snow = result.get("data")[0].get("snow")
            dhi = result.get("data")[0].get("dhi")
            precip = result.get("data")[0].get("precip")
            wind_dir = result.get("data")[0].get("wind_dir")
            max_dhi = result.get("data")[0].get("max_dhi")
            ghi = result.get("data")[0].get("ghi")
            max_temp = result.get("data")[0].get("max_temp")
            t_dni = result.get("data")[0].get("t_dni")
            max_uv = result.get("data")[0].get("max_uv")
            timestamp = result.get("data")[0].get("datetime")
            t_solar_rad = result.get("data")[0].get("t_solar_rad")
            t_dhi = result.get("data")[0].get("t_dhi")
            max_wind_dir = result.get("data")[0].get("max_wind_dir")
            min_temp = result.get("data")[0].get("min_temp")

            db.execute(f"""INSERT INTO public.weather_conditions(
                lat, lon, city_name, rh, ax_wind_spd_ts, t_ghi, max_wind_spd, solar_rad, wind_gust_spd, max_temp_ts, min_temp_ts, clouds, max_dni, precip_gpm, wind_spd, slp, ts, max_ghi, temp, pres, dni, dewpt, snow, dhi, precip, wind_dir, max_dhi, ghi, max_temp, t_dni, max_uv, t_dhi, datetime, t_solar_rad, min_temp, max_wind_dir)
                VALUES ('{lat}', '{lon}', '{city_name}', '{rh}', '{ax_wind_spd_ts}', {t_ghi}, '{max_wind_spd}', '{solar_rad}', '{wind_gust_spd}', '{max_temp_ts}', '{min_temp_ts}', '{clouds}', '{max_dni}', '{precip_gpm}', '{wind_spd}','{slp}', '{ts}', '{max_ghi}', '{temp}', '{pres}', '{dni}', '{dewpt}', '{snow}', '{dhi}', '{precip}', '{wind_dir}', '{max_dhi}', '{ghi}', '{max_temp}', '{t_dni}', '{max_uv}', '{t_dhi}', '{timestamp}', '{t_solar_rad}', '{min_temp}', '{max_wind_dir}');
            """)

save_weather_data_to_db(10)