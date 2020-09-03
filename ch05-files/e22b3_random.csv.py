#!/usr/bin/env python3
"""Solution to chapter 5, exercise 22, beyond 3: random_csv"""


import random
import csv


def random_csv(csv_filename):

    with open(csv_filename, 'w') as output:
        outfile = csv.writer(output)

        for i in range(10):
            output = []
            for j in range(10):
                output.append(random.randint(10, 100))

            outfile.writerow(output)

    for one_line in open(csv_filename):
        numbers = [int(one_item)
                   for one_item in one_line.split(',')]

        print(f'sum = {sum(numbers)}, mean = {sum(numbers)/len(numbers)}')
