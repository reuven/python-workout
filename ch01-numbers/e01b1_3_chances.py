#!/usr/bin/env python3
"""Solution to chapter 1, exercise 1, beyond 1: Guessing game, only 3 chances"""
import random


def guessing_game():
    """Generate a random integer from 1 to 100.

Ask the user repeatedly to guess the number.
Until they guess correctly, tell them to guess higher or lower.
If they take more than three times to guess, the program
tells them that they're out of guesses.
"""
    answer = random.randint(0, 100)
    remaining_guesses = 2

    while remaining_guesses >= 0:
        remaining_guesses -= 1
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')

    else:
        print('Your three chances are up!')
