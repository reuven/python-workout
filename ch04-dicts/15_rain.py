#!/usr/bin/env python3


rainfall = {}

while True:
    city_name = input("Enter city name: ")
    if not city_name:
        break

    mm_rain = input("Enter mm rain: ")
    rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)

for city, rain in rainfall.items():
    print(f"{city}: {rain}")
