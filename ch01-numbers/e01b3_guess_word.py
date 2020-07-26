#!/usr/bin/env python3
"""Solution to chapter 1, exercise 1, beyond 3: Guessing game, words"""
import random

WORDS = [one_word.strip()
         for one_word in open('words.txt')]


def guessing_game():
    """Choose a random word from the dictionary.

Ask the user repeatedly to guess a word.
Until they guess correctly, tell them to guess one that's
earlier or later in the dictionary.
"""
    answer = random.choice(WORDS)

    while True:
        user_guess = int(input('What is your guess? '))

        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break

        if user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')

        else:
            print(f'Your guess of {user_guess} is too high!')
