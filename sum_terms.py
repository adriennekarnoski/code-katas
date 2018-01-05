"""Sum of the first nth term of Series

A function which returns the sum of the series upto nth term(parameter).

#1 Best Practices Solution by kevinplybon (plus 546 more warriors):

def row_sum_odd_numbers(n):
    return n ** 3

"""


def series_sum(n):
    """Takes in n and returns sum of values up to nth term."""
    series_values = [0.00, 1.00]
    if n <= 1:
        return "%.2f" % round(series_values[n], 2)
    x = 4
    while len(series_values) != n + 1:
        series_values.append(1 / x)
        x += 3
    total = "%.2f" % round(sum(series_values), 2)
    return total