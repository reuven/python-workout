#!/usr/bin/env python3
"""Solution to chapter 1, exercise 1: Guessing game"""
import random


def guessing_game():
    """Generate a random integer from 1 to 100.

Ask the user repeatedly to guess the number.
Until they guess correctly, tell them to guess higher or lower.
"""
    answer = random.randint(0, 100)

    while True:
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')
