#!/usr/bin/env python3
"""Solution to chapter 1, exercise 4, beyond 2: name_triangle"""


def name_triangle():
    """Get the user's name. Print a name triangle, starting
with the first letter, then the first two letters, etc.
"""
    name = input("Enter your name: ")

    for i in range(len(name)):
        print(name[:i+1])
