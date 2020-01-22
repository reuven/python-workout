#!/usr/bin/env python3


import operator
people = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

for person in sorted(people, key=operator.itemgetter(1, 0)):
    print("{1:10} {0:10} {2:5.2f}".format(*person))
