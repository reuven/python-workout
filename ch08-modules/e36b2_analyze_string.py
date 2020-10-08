#!/usr/bin/env python3

"""Solution to chapter 8, exercise 36, beyond 2: analyze_string"""


def analyze_string(s):
    output = {'isdigit': 0,
              'isalpha': 0
              'isspace': 0}

    for one_character in s:
        for methodname in output:
            if getattr(one_character, methodname)():  # a sneaky, cool trick!
                output[methodname] += 1

    return output
