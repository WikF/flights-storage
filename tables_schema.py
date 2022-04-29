from google.cloud import bigquery


flights_table = (
    "flights",
    [
        bigquery.SchemaField("flight_number", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("departure_airport", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("arrival_airport", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("fligt_status", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("arrival_planned_time", "TIMESTAMP", mode="REQUIRED"),
        bigquery.SchemaField("departure_planned_time", "TIMESTAMP", mode="REQUIRED"),
        bigquery.SchemaField("arrival_actual_time", "TIMESTAMP", mode="REQUIRED"),
        bigquery.SchemaField("departure_actual_time", "TIMESTAMP", mode="REQUIRED"),
    ],
)

weather_table = (
    "weather",
    [
        bigquery.SchemaField("wind_direction", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("precipitation_in_mm_per_sqm", "NUMERIC", mode="REQUIRED"),
        bigquery.SchemaField("type_of_precipitation", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("visibility", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("temperature", "NUMERIC", mode="REQUIRED"),
    ],
)

#  Metryki dla wybranych lotnisk (granulacja dzienna): średnie opóźnienie przylotu: czas opóźnienia w minutach,
#  lotnisko przylotu, procent opóźnionych lotów, data średnie opóźnienie wylotu: czas opóźnienia w minutach, 
# lotnisko wylotu, procent opóźnionych lotów, data

airport_metrics_table = (
    "airport_metrics",
    [
        bigquery.SchemaField("departure_airport", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("arrival_airport", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("avg_daily_arrival_delay", "NUMERIC", mode="REQUIRED"),
        bigquery.SchemaField("avg_daily_departure_delay", "NUMERIC", mode="REQUIRED"),
        bigquery.SchemaField("%_od_delayed_flights_on_arrival", "NUMERIC", mode="REQUIRED"),
        bigquery.SchemaField("%_od_delayed_flights_on_departure", "NUMERIC", mode="REQUIRED"),
    ],
)

# średnie opóźnienie przylotu: czas opóźnienia w minutach, lotnisko przylotu, procent opóźnionych lotów,
#  miesiąc średnie opóźnienie wylotu: czas opóźnienia w minutach, lotnisko wylotu, procent opóźnionych lotów, data
flight_metrics_table = (
    "flight_metrics",
    [
        bigquery.SchemaField("airline_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("departure_airport", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("arrival_airport", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("avg_daily_arrival_delay", "NUMERIC", mode="REQUIRED"),
        bigquery.SchemaField("avg_daily_departure_delay", "NUMERIC", mode="REQUIRED"),
        bigquery.SchemaField("%_od_delayed_flights_on_arrival", "NUMERIC", mode="REQUIRED"),
        bigquery.SchemaField("%_od_delayed_flights_on_departure", "NUMERIC", mode="REQUIRED"),
    ],
)
