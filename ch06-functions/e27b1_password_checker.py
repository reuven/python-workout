#!/usr/bin/env python3

"""Solution to chapter 6, exercise 27, beyond 1: password_checker"""

import string


def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    uppercase_set = set(string.ascii_uppercase)
    lowercase_set = set(string.ascii_lowercase)
    punctuation_set = set(string.punctuation)
    digits_set = set(string.digits)

    def check_password(password):

        if len([one_character
                for one_character in password
                if one_character in uppercase_set]) < min_uppercase:
            print(f'Not enough uppercase letters; min is {min_uppercase}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in lowercase_set]) < min_lowercase:
            print(f'Not enough lowercase letters; min is {min_lowercase}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in punctuation_set]) < min_punctuation:
            print(f'Not enough punctuation; min is {min_punctuation}')
            return False
        elif len([one_character
                  for one_character in password
                  if one_character in digits_set]) < min_digits:
            print(f'Not enough digits; min is {min_digits}')
            return False
        else:
            return True
    return check_password
