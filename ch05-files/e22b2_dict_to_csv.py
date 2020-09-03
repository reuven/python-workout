#!/usr/bin/env python3
"""Solution to chapter 5, exercise 22, beyond 2: dict_to_csv"""


import csv


def dict_to_csv(d, csv_filename):

    with open(csv_filename, 'w') as output:
        outfile = csv.writer(output, delimiter=delimiter)

        for key, value in d.items():
            outfile.writerow([key, value, type(value)])
