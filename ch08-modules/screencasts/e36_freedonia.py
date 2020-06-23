RATES = {
    'Chico': 0.5,
    'Groucho': 0.7,
    'Harpo': 0.5,
    'Zeppo': 0.4
}


def time_percentage(hour):
    return hour / 24


def calculate_tax(amount, state, hour):
    return amount + (amount * RATES[state] * time_percentage(hour))
