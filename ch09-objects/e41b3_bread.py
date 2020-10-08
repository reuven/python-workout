#!/usr/bin/env python3

"""Solution to chapter 9, exercise 41, beyond 3: bread"""


class Bread:
    def __init__(self):
        # nutrition per slice
        self.calories = 66
        self.carbs = 12
        self.sodium = 170
        self.sugar = 1
        self.fat = 0.8

    def get_nutrition(self, number_of_slices):
        return {key: value*number_of_slices
                for key, value in vars(self).items()}


class WholeWheatBread(Bread):
    def __init__(self):
        self.calories = 67
        self.carbs = 12
        self.sodium = 138
        self.sugar = 1.4
        self.fat = 1


class RyeBread(Bread):
    def __init__(self):
        self.calories = 67
        self.carbs = 12
        self.sodium = 172
        self.sugar = 1
        self.fat = 0.8
