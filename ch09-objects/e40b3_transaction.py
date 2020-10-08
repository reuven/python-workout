#!/usr/bin/env python3

"""Solution to chapter 9, exercise 40, beyond 3: transactions"""


class Transaction:
    balance = 0

    def __init__(self, amount):
        self.amount = amount
        Transaction.balance += amount
