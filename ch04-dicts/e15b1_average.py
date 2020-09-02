#!/usr/bin/env python3
"""Solution to chapter 4, exercise 15, beyond 1: rainfall with averages"""


def get_rainfall():
    rainfall = {}

    while True:
        city_name = input('Enter city name: ')
        if not city_name:
            break

        mm_rain = input('Enter mm rain: ')

        if city_name not in rainfall:
            rainfall[city_name] = []

        rainfall[city_name].append(int(mm_rain))

    for city, rain in rainfall.items():
        print(f'{city}: Total {sum(rain)}, Average {sum(rain)/len(rain)}')
