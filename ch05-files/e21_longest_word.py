#!/usr/bin/env python3


import os
dirname = input("Enter a directory name: ")


def find_longest_word(filename):
    longest_word = ''
    for one_line in open(filename):
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
                longest_word = one_word
    return longest_word


print({filename: find_longest_word(os.path.join(dirname, filename)) < 1 >
       for filename in os.listdir(dirname) < 2 >
       if os.path.isfile(os.path.join(dirname, filename))}) < 3 >
