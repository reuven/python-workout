#!/usr/bin/env python3

"""Solution to chapter 9, exercise 42, beyond 2: recent_dict"""


class RecentDict(dict):
    def __init__(self, maxsize):
        super().__init__()
        self.maxsize = maxsize

    def __setitem__(self, key, value):
        dict.__setitem__(self, str(key), value)

        if len(self) > self.maxsize:
            self.pop(list(self.keys())[0])
