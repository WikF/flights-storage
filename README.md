# flights-storage

1. Baza danych:
    - Baza danych której użyłem to Postgres 
2. Źródła danych (API)
API dla statusów lotów: 
Użyłem KLM flights API [link](https://developer.airfranceklm.com/documentations/api/A000042)
API pogodowe:
W celu pobrania danych historyczny użyłem API weather bit, które pozwala pobrać pogodę dla danej lokalizacji w określonym czasie [link](https://www.weatherbit.io/api/weather-history-hourly)
W celu pobrania danych bieżących zdywersyfikowałem źródła dancyh ze względu na limity zapytań do API. 
Korzystam z weatherbit [link](https://weather.visualcrossing.com/)
3. Skrypty do pobrania danych. 
-   Aby pobrać dane pogodowe dla poszczególnych lotó stworzyłem pośrednią tabele w bazie danych która zawiera pogodę tylko dla danej lokalizacji oraz godziny. 
4. Cron jobs- Mechanizm odpalajacy cyklicznie skrypty zapisujące do bazy danych.
5. ML model - model uczenia maszynowego, przyjmujący za parametry dane lotnicze i dane pogodowe i zwracający status lotu.
6. Predicting funcionality - mrchanizm który pobierze argumenty od użytkownika, odpyta model ML i zwróci rezultat - czy lot będzie opóźniony czy nie 
7. UI - zadaniem interfejsu użytkownika będzie zaprezentowanie mu watsty wizualnej przez którą bęzdie mógł podać parametry dla modelu ML przewidującego opóźnienia lotnicze. 

Zrzuty z ekranu z bazy danych:

Tabele:

<img width="294" alt="tabele" src="https://user-images.githubusercontent.com/25872760/175573838-81b3c825-d7ac-49f4-99c0-43753ccd8d92.PNG">

Tabela weather conditions:

<img width="1068" alt="weather conditions" src="https://user-images.githubusercontent.com/25872760/175573833-1708ed3a-a358-4fc9-8b78-f00177003610.PNG">

Tabela flights:

<img width="1080" alt="flights" src="https://user-images.githubusercontent.com/25872760/175573836-3ed6d584-117b-4804-8a63-c6ac3f910e2d.PNG">

[Przykładowa odpowiedź z weather crossing](https://github.com/WikF/flights-storage/blob/main/weather.json)

[Przykładowa odpowiedź z weatherbit](https://github.com/WikF/flights-storage/blob/main/weather_history.json)

[Przykładowa odpowiedź z KLM API](https://github.com/WikF/flights-storage/blob/main/klm_flights.json)

Mechanizmy zapisujące dane do bazy: 

[Historia pogody](https://github.com/WikF/flights-storage/blob/main/weather_history.py)
[Bieżąca pogoda](https://github.com/WikF/flights-storage/blob/main/weather_feather.py)
[Loty KLM](https://github.com/WikF/flights-storage/blob/main/save_flights_from_files_to_db.py)

