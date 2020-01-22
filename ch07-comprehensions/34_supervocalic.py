#!/usr/bin/env python3


def get_sv(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    return {word.strip()
            for word in open(filename)
            if vowels < set(word.lower())}


print(get_sv('/usr/share/dict/words'))
