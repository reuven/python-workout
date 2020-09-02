#!/usr/bin/env python3
"""Solution to chapter 4, exercise 14: beyond 2: temps"""

from datetime import datetime, timedelta


TEMPS = {'2020-08-16': 30,
         '2020-08-17': 32,
         '2020-08-18': 32,

         }


def temps():
    while True:
        today = input("Enter date in YYYY-MM-DD format:").strip()

        if not today:
            break

        if len(today) != 10:
            print(f'Invalid format; try again. ')
            continue

        if today.count('-') != 2:
            print(f'Invalid format; try again. ')
            continue

        if today not in TEMPS:
            print(f'The date {today} is unknown; try again. ')
            continue

        try:
            today_date = datetime.fromisoformat(today).date()
        except ValueError as e:
            print(f'Not a valid date string; try again. ')
            continue

        yesterday_date = str(today_date - timedelta(1))
        tomorrow_date = str(today_date + timedelta(1))

        print(f'{yesterday_date}: {TEMPS.get(yesterday_date, "No data available")}')
        print(f'{today_date}: {TEMPS[str(today_date)]}')
        print(f'{tomorrow_date}: {TEMPS.get(tomorrow_date, "No data available")}')
