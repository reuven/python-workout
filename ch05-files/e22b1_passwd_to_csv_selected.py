#!/usr/bin/env python3
"""Solution to chapter 5, exercise 22, beyond 1: passwd_to_csv_selected"""


import csv


def passwd_to_csv(passwd_filename, csv_filename, fields_to_pass='1 2', delimiter='\t'):
    fields_to_pass = [int(one_item)
                      for one_item in fields_to_pass]

    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter=delimiter)
        for record in infile:

            if len(record) > 1:
                fields = [one_field
                          for index, one_field in enumerate(record)
                          if index in fields_to_pass]

                outfile.writerow(*fields)
