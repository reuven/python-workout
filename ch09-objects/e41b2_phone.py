#!/usr/bin/env python3

"""Solution to chapter 9, exercise 41, beyond 2: phone"""


class Phone:
    def __init__(self):
        pass

    def dial(self, number):
        return f'Dialing {number}'


class SmartPhone(Phone):
    def run_app(self, app_name):
        return f'Running an app: {app_name}'


class iPhone(SmartPhone):
    def run_app(self, app_name):
        return super().run_app(app_name).lower()
