from db_utils.create_tables import db

import json

flight_numbers=[]
import os
for root, dirs, files in os.walk("../jsons"):
    for name in files:
        with open(f'jsons/{name}') as f:
            data = list(json.load(f).items())
            data=data[0][1]
            for i in data:
                flight_id = i.get("id")
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
                departure_datetime = i.get("flightLegs")[number_of_legs - 2].get("departureInformation").get("times").get("scheduled")
                flight = db.execute(f"""insert into flights(flight_id, flight_number, airline_name, number_of_legs, flight_status, arrival_longitude,
                    arrival_lattitude, arrival_airport_name, arrival_datetime, departure_longitude,departure_lattitude,
                    departure_airport_name, departure_datetime) values('{flight_id}', '{flight_number}', '{airline_name}', '{number_of_legs}', '{flight_status}', '{arrival_longitude}',
                    '{arrival_lattitude}', '{arrival_airport_name}', '{arrival_datetime}', '{departure_longitude}', '{departure_lattitude}',
                    '{departure_airport_name}', '{departure_datetime}')        On CONFLICT(flight_id) DO NOTHING;
                    """)

print(sorted(flight_numbers))