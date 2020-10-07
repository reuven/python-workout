#!/usr/bin/env python3

"""Solution to chapter 7, exercise 35b, beyond 3: currency_conversion"""


def currency_conversion(books, new_currency):
    return {title: {'first': name.split()[0],
                    'last': name.split()[1],
                    'price': price * conversions[new_currency]}
            for name, title, price in books}
