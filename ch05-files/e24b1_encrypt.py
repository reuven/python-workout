#!/usr/bin/env python3
"""Solution to chapter 5, exercise 24, beyond 1: encrypt"""


def encrypt(filename, text):
    with open(filename, 'w') as outfile:
        for one_character in text:
            outfile.write(f'{ord(one_character)}\n')


def decrypt(filename):
    characters = [chr(int(one_character))
                  for one_character in open(filename)
                  if one_character.strip().isdigit()]
    return ''.join(characters)
