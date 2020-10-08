#!/usr/bin/env python3

"""Solution to chapter 8, exercise 37, beyond 2: selftest (in a package)"""


def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(f'Enter an option ({option_string}): ')
        if choice in options:
            return options[choice]()

        print('Not a valid option')
