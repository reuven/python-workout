#!/usr/bin/env python3


filename = input("Enter a filename: ")
final_line = ''
for current_line in open(filename):
    final_line = current_line
print(final_line, end='')
