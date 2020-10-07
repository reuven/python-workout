#!/usr/bin/env python3

"""Solution to chapter 7, exercise 29, beyond 2: increment_area_code"""


def increment_area_code(full_phone_number):
    area_code, phone_number = full_phone_number.split('-', 1)

    if area_code[0] in '012345':
        area_code = str(int(area_code) + 1)

    return f'{area_code}-{phone_number}'


def increment_all_area_codes(area_codes):
    return [increment_area_code(one_phone_number)
            for one_phone_number in area_codes]
