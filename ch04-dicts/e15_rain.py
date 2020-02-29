#!/usr/bin/env python3
"""Solution to chapter 4, exercise 15: rainfall"""


def get_rainfall():
    """Ask the user repeatedly for a city name and mm of rainfall.

If the city is blank, then stop asking questions,
and report all cities and rainfall.

Otherwise, ask for rainfall and add the current rainfall
to any previous report for that city.
"""

    rainfall = {}

    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break

        mm_rain = input('Enter mm rain: ')
        rainfall[city_name] = rainfall.get(city_name, 0) + int(mm_rain)

    for city, rain in rainfall.items():
        print(f'{city}: {rain}')
