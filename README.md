# flights-storage
Data platform gathering data from free flights API and serving it to the world in structured way on premise.
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

