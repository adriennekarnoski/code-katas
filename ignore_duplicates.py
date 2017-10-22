"""Kata: Sum a list but ignore any duplicates
Writes a function that sums a list,
but ignores any duplicate items in the list.


#1 Best Practices Solution by zebulan, ExhaleO2, DCoulter:

from collections import Counter


def sum_no_duplicates(nums):
    return sum(k for k, v in Counter(nums).items() if v == 1)

"""


def sum_no_duplicates(numbers):
    """Takes list of numbers and ignores duplicates \
    then gets the sum of numbers remaining."""
    total = 0
    for number in numbers:
        result = numbers.count(number)
        if result >= 2:
            print(number)
        else:
            total += number
    return total