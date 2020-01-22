#!/usr/bin/env python3


word = input("Enter a word: ")

output = []
for letter in word:
    if letter in 'aeiou':
        output.append(f'ub{letter}')
    else:
        output.append(letter)

print(''.join(output))
