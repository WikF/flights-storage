import logging

import psycopg2
from psycopg2.extras import LoggingConnection


def create_tables():
    create_flights = """CREATE TABLE IF NOT EXISTS 
               flights (
                flight_id text primary key,
                flight_number text,
                airline_name text, 
                number_of_legs int, 
                flight_status text, 
                arrival_longitude  text,
                arrival_lattitude  text, 
                arrival_airport_name text, 
                arrival_datetime text,
                departure_longitude  text,
                departure_lattitude  text, 
                departure_airport_name text, 
                departure_datetime text
               )"""

    create_weather_conditions = """CREATE TABLE IF NOT EXISTS 
               weather_conditions (
             lat text,
             lon text,
             city_name text,
             rh text , 
             ax_wind_spd_ts text,
             t_ghi text,
             max_wind_spd text,
             solar_rad text,
             wind_gust_spd text,
             max_temp_ts text ,
             min_temp_ts text,
             clouds text,
             max_dni text,
             precip_gpm text,
             wind_spd text,
             slp text,
             ts text,
             max_ghi text,
             temp text,
             pres text,
             dni text,
             dewpt text,
             snow text,
             dhi text,
             precip text,
             wind_dir text,
             max_dhi text,
             ghi text,
             max_temp text,
             t_dni text,
             max_uv text,
             t_dhi text,
             datetime text,
             t_solar_rad text,
             min_temp text, 
             max_wind_dir text
        )"""
    create_data_to_featch = """
        CREATE OR REPLACE VIEW
    data_to_fetch_weather as 
    select
    distinct
    flight_id,
    arrival_lattitude as lat, arrival_longitude
    lon, arrival_datetime::timestamptz as datetime
    from flights
    union
    all
    select
    flight_id,
    departure_lattitude, departure_longitude,
    departure_datetime::timestamptz
    at
    time
    zone
    'utc'
    from flights"""

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("loggerinformation")

    ml_db = psycopg2.connect("postgres://postgres@localhost:5433/pgml_development",
                             connection_factory=LoggingConnection)
    ml_db.initialize(logger)
    with ml_db.cursor() as curs:
        curs.execute(create_data_to_featch)
        curs.execute(create_weather_conditions)
        curs.execute(create_flights)


create_tables()
