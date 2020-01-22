#!/usr/bin/env python3

import random


def create_password_generator(characters):
    def create_password(length):
        output = []

        for i in range(length):
            output.append(random.choice(characters))
        return ''.join(output)
    return create_password
