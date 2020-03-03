#!/usr/bin/env python3
"""Solution to chapter 5, exercise 22: passwd_to_csv"""


import csv


def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        r = csv.reader(passwd, delimiter=':')
        w = csv.writer(output, delimiter='\t')
        for record in r:
            if len(record) > 1:
                w.writerow((record[0], record[2]))
