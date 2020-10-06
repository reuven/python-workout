#!/usr/bin/env python3
"""Solution to chapter 5, exercise 24, beyond 2: vowels_and_consonants"""

import string


def vowels_and_consonants(infilename, vowel_filename, consonant_filename):
    with open(infilename) as infile, open(vowel_filename, 'w') as vowel_out, open(consonant_filename, 'w') as consonant_out:
        for one_line in infile:
            for one_character in one_line:
                if one_character.lower() in 'aeiou':
                    vowel_out.write(one_character)
                elif one_character.lower() in string.ascii_lowercase:
                    consonant_out.write(one_character)
