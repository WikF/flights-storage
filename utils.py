import logging

import psycopg2
from psycopg2.extras import LoggingConnection


def insert_flight_data_to_db(api_response, table='flights'):
    flight_numbers = []
    if api_response.get('operationalFlights'):
        response = api_response['operationalFlights']
    else:
        response = [api_response]
    for i in response:
        flight_id = i.get("id")
        flight_number = i.get("flightNumber")
        flight_number = i.get("flightNumber")
        flight_numbers.append(flight_number)
        airline_name = i.get("airline").get("name")
        number_of_legs = len(i.get("route"))
        flight_status = i.get("flightStatusPublic")
        arrival_longitude = i.get("flightLegs")[0].get("arrivalInformation").get("airport").get(
            "location").get("longitude")
        arrival_lattitude = i.get("flightLegs")[0].get("arrivalInformation").get("airport").get(
            "location").get("latitude")
        arrival_airport_name = i.get("flightLegs")[0].get("arrivalInformation").get("airport").get("code")
        arrival_datetime = i.get("flightLegs")[0].get("arrivalInformation").get("times").get("scheduled")
        departure_longitude = i.get("flightLegs")[number_of_legs - 2].get("departureInformation").get(
            "airport").get("location").get("longitude")
        departure_lattitude = i.get("flightLegs")[number_of_legs - 2].get("departureInformation").get(
            "airport").get("location").get("latitude")
        departure_airport_name = i.get("flightLegs")[number_of_legs - 2].get("departureInformation").get(
            "airport").get("code")
        departure_datetime = i.get("flightLegs")[number_of_legs - 2].get("departureInformation").get("times").get(
            "scheduled")
        flight = f"""insert into {table} (flight_id, flight_number, airline_name, number_of_legs, flight_status, arrival_longitude,
        arrival_lattitude, arrival_airport_name, arrival_datetime, departure_longitude,departure_lattitude,
        departure_airport_name, departure_datetime) values('{flight_id}', '{flight_number}', '{airline_name}', '{number_of_legs}', '{flight_status}', '{arrival_longitude}',        '{arrival_lattitude}', '{arrival_airport_name}', '{arrival_datetime}', '{departure_longitude}', '{departure_lattitude}','{departure_airport_name}', '{departure_datetime}')        On CONFLICT(flight_id) DO NOTHING;"""

        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger("loggerinformation")

        ml_db = psycopg2.connect("postgres://postgres@localhost:5433/pgml_development")
        with ml_db.cursor() as curs:
            curs.execute(flight)
        ml_db.commit()
        ml_db.close()
