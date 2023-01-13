import time

import schedule
from klm_flights import flights
from weather_utils import save_weather_data_to_db


try:
    save_weather_data_to_db(900)
finally:
    print('done')

try:
    flights(900)
except:
    print('now weather')