#!/usr/bin/env python3
"""Solution to chapter 1, exercise 3, beyond 2: decimal_add"""

from decimal import Decimal


def decimal_add(first, second):
    """Accepts two strings, turns them into decimals, and returns a float
representing the sum of these two.
"""
    return float(Decimal(first) + Decimal(second))
