#!/usr/bin/env python3
"""Solution to chapter 5, exercise 19, beyond 2: factors"""

from collections import defaultdict


def factors():
    output = defaultdict(list)

    numbers = input("Enter numbers, separated by spaces: ").split()

    for one_number in numbers:
        if not one_number.isdigit():
            print(f'Ignoring {one_number}')
            continue

        one_number = int(one_number)
        for i in range(1, one_number):
            if not one_number % i:
                output[one_number].append(i)

        output[one_number].append(one_number)

    return output
