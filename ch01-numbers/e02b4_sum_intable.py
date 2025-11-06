#!/usr/bin/env python3
# Solution to chapter 1, exercise 2, beyond 4: sum intable
# Write a function that takes a list of Python objects. Sum the objects that either
# are integers or can be turned into integers, ignoring the others.

def sum_ignore(liste: list):
    total = 0
    for number in liste:
        try:
            valeur = int(number)
            total += valeur
        except (ValueError, TypeError):
            continue
    return total
