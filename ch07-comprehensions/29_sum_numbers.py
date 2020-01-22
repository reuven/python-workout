#!/usr/bin/env python3

numbers = input("Enter integers, separated by spaces: ")

total = sum(int(number)
            for number in numbers.split()
            if number.isdigit())

print(f"Sum: {total}")
