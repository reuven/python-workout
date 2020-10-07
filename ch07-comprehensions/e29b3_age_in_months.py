#!/usr/bin/env python3

"""Solution to chapter 7, exercise 29, beyond 3: age_in_months"""


def age_in_months(list_of_people):
    return [dict(**one_person, age_in_months=one_person['age'] * 12)
            for one_person in mylist
            if one_person['age'] <= 20]
