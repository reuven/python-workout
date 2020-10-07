#!/usr/bin/env python3

"""Solution to chapter 7, exercise 35a, beyond 3: cities"""

import json


def get_city_data(filename):
    return {one_city['city']: one_city['population']
            for one_city in json.load(open(filename))
            }


def get_city_data2(filename):
    return {(one_city['city'], one_city['state']): one_city['population']
            for one_city in json.load(open(filename))
            }
