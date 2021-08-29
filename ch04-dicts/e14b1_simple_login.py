#!/usr/bin/env python3
"""Solution to chapter 4, exercise 14: beyond 1: simple_login"""


USERS = {'root': '1234', 'ceo': '!!!!!', 'reuven': 'GrEaTpW?'}


def login():
    while True:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        if USERS.get(username) == password:
            return True

        else:
            return False
