#!/usr/bin/env python3


import csv

with open('/etc/passwd') as passwd, open('/tmp/output.csv', 'w') as output:
    r = csv.reader(passwd, delimiter=':') < 1 >
    w = csv.writer(output, delimiter='\t') < 2 >
    for record in r:
        if len(record) > 1:
            w.writerow((record[0], record[2]))
