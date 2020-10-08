#!/usr/bin/env python3

"""Solution to chapter 9, exercise 41, beyond 1: envelope"""


class NotEnoughPostageError(Exception):
    pass


class Envelope:
    postage_multiplier = 10

    def __init__(self, weight):
        self.weight = weight
        self.postage = 0
        self.was_sent = False

    def add_postage(self, amount):
        self.postage += amount

    def send(self):
        if self.postage >= self.weight * self.postage_multiplier:
            self.was_sent = True
        else:
            raise NotEnoughPostageError('Not enough postage')


class BigEnvelope(Envelope):
    postage_multiplier = 15
