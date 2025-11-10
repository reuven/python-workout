"""Solution to chapter 3, exercise 10, beyond 1: mysum_bigger_than"""

from typing import Tuple, Union

def mysum_bigger_than(*args: Tuple[Union[int, float, str, list]]):
     """
     Sum items, which should be of the same type.
    Ignore any below the value of threshold.
    The arguments should handle the + operator.
    If passed no arguments, then return an empty tuple.
    """

    if not args:
        return args

    first_element = args[0]

    # Initialize output based on the type of first_element
    if isinstance(first_element, (int, float)):
        output = 0
    elif isinstance(first_element, str):
        output = ""
    elif isinstance(first_element, list):
        output = []
    else:
        return None  # In case an unsupported type is passed.

    for element in args[1:]:
        if element > first_element:
            output += element

    return output

# Test cases
print(mysum_bigger_than([1, 2, 3], [4, 5, 6], [23, 52]))  # Expecting [4, 5, 6] + [23, 52]
print(mysum_bigger_than(1, 2, 3))                        # Expecting 2 + 3
print(mysum_bigger_than('abc', 'def', 'ghi'))             # Expecting 'def' + 'ghi'


