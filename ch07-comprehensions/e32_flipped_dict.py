#!/usr/bin/env python3


d = {'a': 1, 'b': 2, 'c': 3}
flipped_d = {value: key
             for key, value in d.items()}
print(flipped_d)
