"""Kata: Sum of odd numbers

Given the triangle of consecutive odd numbers \
calculate the row sums of this triangle from the row index.

#1 Best Practices Solution by kevinplybon (plus 546 more warriors):

def row_sum_odd_numbers(n):
    return n ** 3

"""


def row_sum_odd_numbers(n):
    """function takes in number and returns sum of numbers in that row."""
    calculate_index = sum([num for num in range(1, n)])
    odd_numbers = []
    m = 1
    while len(odd_numbers) != calculate_index + n:
        odd_numbers.append(m)
        m += 2
    numbers = []
    for i in range(calculate_index, calculate_index + n):
        numbers.append(odd_numbers[i])
    return sum(numbers)