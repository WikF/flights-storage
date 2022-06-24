import postgresql

db = postgresql.open("pq://postgres:password@localhost/flights_predictor")


def create_tables():

    db.execute("""CREATE TABLE IF NOT EXISTS 
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
               )""")

    db.execute("""CREATE TABLE IF NOT EXISTS 
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
        )""")
    db.execute("""CREATE TABLE IF NOT EXISTS
    data_to_fetch_weather_hist as 
    select
    distinct
    arrival_lattitude as lat, arrival_longitude
    lon, arrival_datetime::timestamptz as datetime
    from flights
    union
    all
    select
    departure_lattitude, departure_longitude,
    departure_datetime::timestamptz
    at
    time
    zone
    'utc'
    from flights""")
create_tables()