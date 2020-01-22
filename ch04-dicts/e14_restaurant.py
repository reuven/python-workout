#!/usr/bin/env python3


menu = {'sandwich': 10, 'tea': 7, 'salad': 9}

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
