#!/usr/bin/env python3

d = 0
h = input("Enter a hex number to convert to decimal: ")
for power, digit in enumerate(reversed(h)):
    d += int(digit, 16) * (16 ** power)
print(d)
