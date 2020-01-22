#!/usr/bin/env python3

number_of_runs = 0
total_time = 0

while True:
    one_run = input("Enter 10 km run time, or 'q' to exit: ")

    if one_run == 'q':
        break

    else:
        number_of_runs += 1
        total_time += float(one_run)

average_time = total_time / number_of_runs

print(f"Average of {average_time}, over {number_of_runs} runs")
