#!/usr/bin/env python3
"""Solution to chapter 1, exercise 3: run_timing"""


def run_timing():
    """Asks the user repeatedly for numeric input.
Prints the average time and number of runs.
"""

    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 km run time: ')

        if not one_run:
            break

        number_of_runs += 1
        total_time += float(one_run)

    average_time = total_time / number_of_runs

    print(f'Average of {average_time}, over {number_of_runs} runs')
