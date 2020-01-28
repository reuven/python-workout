#!/usr/bin/env python3
"""Solution to chapter 4, exercise 14: restaurant"""


menu = {'sandwich': 10, 'tea': 7, 'salad': 9}


def restaurant():
    """Ask the user to enter their dining preferences, one by one, based
on the global "menu" dict. 

- If the user enters an empty string, stop asking and print the total bill.
- If the user enters something on the menu (i.e., a key in "menu"), then
  print the price and the total.
- If the user enters something not on the menu, then tell them the item isn't
  available.
"""

    total = 0
    while True:
        order = input("Order: ").strip()

        if not order:
            break

        elif order in menu:
            price = menu[order]
            total += price
            print(f'{order} costs {price}, total is {total}')

        else:
            print(f'We are fresh out of {order} today')

    print(f'Your total is {total}')
