#!/usr/bin/env python3

"""Solution to chapter 9, exercise 39, beyond 2: has_book"""


class TooManyBookOnShelfError(Exception):
    pass


class Book:
    def __init__(self, title, author, price, width):
        self.title = title
        self.author = author
        self.price = price
        self.width = width


class Shelf:
    def __init__(self, width):
        self.books = []
        self.width = width

    def add_books(self, *args):
        for new_book in args:
            if self.total_width() + new_book.width > self.width:
                raise TooManyBookOnShelfError('Too many books!')
            self.books.append(new_book)

    def total_price(self):
        return sum(one_book.price
                   for one_book in self.books)

    def has_book(self, title):
        return title in (one_book.title
                         for one_book in self.books)

    def total_width(self):
        return sum(one_book.width
                   for one_book in self.books)
