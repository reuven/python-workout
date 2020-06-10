#!/usr/bin/env python3

"""Solution to chapter 8, exercise 37: menu"""


def menu(**options):
    """Function that takes keyword arguments. The value
associated with each key is a function taking zero arguments.

The user is asked to enter input.

If the input matches a keyword, then the associated function
is invoked, and its return value is returned to the user.

If the input doesn't match a keywork, the user is asked to
try again.
"""
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()

        print('Not a valid option')
