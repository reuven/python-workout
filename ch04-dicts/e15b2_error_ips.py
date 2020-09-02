#!/usr/bin/env python3
"""Solution to chapter 4, exercise 15, beyond 2: errors with IP addresses"""

from collections import defaultdict


def error_ip_addresses(filename):
    output = defaultdict(list)

    for one_line in open(filename):
        fields = one_line.split()
        ip_address = fields[0]
        response_code = fields[8]
        output[response_code].append(ip_address)

    return output
