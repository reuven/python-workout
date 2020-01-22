#!/usr/bin/env python3


import operator
operations = {'+': operator.add,
              '-': operator.sub,
              '*': operator.mul,
              '/': operator.truediv,
              '**': operator.pow,
              '%': operator.mod}

to_solve = input("Enter a two-operand math problem, with prefix notation: ")

operator, first_s, second_s = to_solve.split()
first = int(first_s)
second = int(second_s)

print(operations[operator](first, second))
