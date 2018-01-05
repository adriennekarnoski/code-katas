"""Kata: Sum of two lowest positive integers - \
A function that returns the sum of the two lowest positive numbers \
given an array of minimum 4 integers.

#1 Best Practices Solution by danman1979 (plus 356 more warriors):

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

"""


def sum_two_smallest_numbers(numbers):
    """The function that calculates the sum of lowest numbers."""
    order = sorted(numbers, key=int)
    return order[0] + order[1]

