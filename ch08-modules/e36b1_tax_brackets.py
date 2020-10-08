#!/usr/bin/env python3

"""Solution to chapter 8, exercise 36, beyond 1: tax_brackets"""


brackets = [{'start': 0, 'end': 1000, 'tax': 0},
            {'start': 1000, 'end': 10000, 'tax': .1},
            {'start': 10000, 'end': 20000, 'tax': .2},
            {'start': 20000, 'end': 999999999999, 'tax': .5}]


def tax_brackets(amount, brackets):
    tax_owed = 0

    for one_bracket in brackets:
        if amount < one_bracket['start']:
            continue

        taxed_amount = min(amount, one_bracket['end'])
        taxed_amount -= one_bracket['start']

        tax_owed += taxed_amount * one_bracket['tax']

    return tax_owed
