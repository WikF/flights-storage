import logging
import psycopg2
from psycopg2.extras import LoggingConnection

sql_pre_data = """CREATE VIEW public.data_prepared AS
SELECT flight_id,
  dense_rank() over (order by airline_name desc) as airline_category,
  CAST(number_of_legs AS FLOAT4) as number_of_legs,
  dense_rank() over ( order by (case when flight_status like '%CANCELLED%' THEN 'CANCELLED 'else 'ARRIVED' END)  desc) -1 as flight_status_category,
  CAST(arrival_longitude AS FLOAT4),
  CAST(arrival_lattitude AS FLOAT4),
  dense_rank() over (order by arrival_airport_name desc) as arrival_airport_name_category,
  CAST(EXTRACT( MONTH FROM CAST(ARRIVAL_DATETIME AS TIMESTAMP)) AS FLOAT4) AS ARRIVAL_MONTH,
  CAST(EXTRACT(DOW FROM CAST(ARRIVAL_DATETIME AS TIMESTAMP)) AS FLOAT4) AS ARRIVAL_DOW,
  CAST(EXTRACT(DOW FROM CAST(ARRIVAL_DATETIME AS TIMESTAMP)) AS FLOAT4) AS ARRIVAL_WEEK,
  CAST(departure_longitude AS FLOAT4),
  CAST(departure_lattitude AS FLOAT4),
  dense_rank() over (order by departure_airport_name desc) as departure_airport_name_category,
  CAST(EXTRACT(MONTH FROM CAST(DEPARTURE_DATETIME AS TIMESTAMP)) AS FLOAT4) DEPARTURE_MONTH,
  CAST(EXTRACT(DOW FROM CAST(DEPARTURE_DATETIME AS TIMESTAMP)) AS FLOAT4) AS DEPARTURE_DOW,
  CAST(EXTRACT(week FROM CAST(DEPARTURE_DATETIME AS TIMESTAMP)) AS FLOAT4) AS DEPARTURE_WEEK,
    dense_rank() over (order by visibility desc) as visibility_category,
	dense_rank() over (order by winddir desc) as winddir_category,
    dense_rank() over (order by conditions desc) as conditions_category,
    dense_rank() over (order by windspeed desc) as windspeed_category,
    dense_rank() over (order by precip desc) as precip_category,
    dense_rank() over (order by "temp" desc) as temp_category
  FROM flights
  LEFT JOIN weather_hist on ((flights.arrival_longitude = lon and flights.arrival_lattitude = lat and to_char(timestamptz(arrival_datetime), 'yyyy-mm-dd')=left(datetime, 10))
  or (flights.departure_longitude=lon and  flights.departure_lattitude=lat and  to_char(timestamptz(departure_datetime), 'yyyy-mm-dd')=left(datetime, 10)));"""

#
# train_model = """SELECT * FROM pgml.train('Flight classification',
# 	task => 'classification',
#     relation_name => 'data_prepared_for_model',
#     y_column_name => 'flight_status_category',
#     algorithm => 'xgboost');"""


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("loggerinformation")
ml_db = psycopg2.connect("postgres://postgres@localhost:5433/pgml_development")

with ml_db.cursor() as curs:
    curs.execute(sql_pre_data)

ml_db.commit()
ml_db.close()

    # curs.execute(train_model)
# leaving contexts doesn't close the connection

# cur.execute(train_model)



# query to predict
"""
SELECT *,
    pgml.predict(
    'Flight classification',         
        ARRAY[
            airline_category, number_od_legs,arrival_longitude, arrival_lattitude, arrival_airport_name_category,
			arrival_month, arrival_dow, arrival_week, departure_longitude, departure_lattitude, departure_airport_name_category,
			departure_month, departure_dow, departure_week, visibility_category, winddir_category, conditions_Category, windspeed_category, 
			precip_category, temp_category
        ]
    ) AS b
FROM data_prepared d where flight_id like '20221229%' 
LIMIT 25;"""