#!/usr/bin/env python3

"""Solution to chapter 7, exercise 35b, beyond 2: books"""


def make_book_dict(books):

    return {title: {'first': name.split()[0],
                    'last': name.split()[1],
                    'price': price}
            for name, title, price in books}
