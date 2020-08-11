#!/usr/bin/env python3
"""Solution to chapter 2, exercise 6, beyond 3: IP addresses with 404"""


def ips_for_404s(filename):
    """Given the name of an Apache logfile,
print the IP address where the response code
is 4040

"""
    for one_line in open(filename):
        if ' 404 ' in one_line:
            print(one_line.split()[0])
