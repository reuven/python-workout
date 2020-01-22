#!/usr/bin/env python3

import operator

people = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}
          ]


for person in sorted(people, key=operator.itemgetter('last', 'first')):
    print(f"{person['last']}, {person['first']}: {person['email']}")
