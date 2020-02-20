#!/usr/bin/env python3

"""Solution to chapter 6, exercise 27: makepw"""

import random


def create_password_generator(characters):
    """This function takes a string as input.

It returns a function that, when invoked with an
integer argument, returns a string containing
a random selection from "characters", of length
"length".
"""
    def create_password(length):
        output = []

        for i in range(length):
            output.append(random.choice(characters))
        return ''.join(output)
    return create_password
