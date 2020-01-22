#!/usr/bin/env python3


def transform_values(func, d):
    return {key: func(value)
            for key, value in d.items()}
