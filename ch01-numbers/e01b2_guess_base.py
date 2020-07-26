#!/usr/bin/env python3
"""Solution to chapter 1, exercise 1, beyond 2: Guessing game, number bases"""
import random


def guessing_game():
    """Generate a random integer from 1 to 100.

Ask the user repeatedly to guess the number.
Until they guess correctly, tell them to guess higher or lower.

The program chooses a random number base for the user's input,
as well as a random number.

NOTE: This game might be considered torture under the Geneva conventions.
"""
    answer = random.randint(0, 100)
    required_base = random.choice([2, 8, 10, 16])  # binary/octal/decimal/hex

    while True:
        user_guess = int(input('What is your guess? '), required_base)

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')
