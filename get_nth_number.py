"""Get Nth Even Number

Return the Nth Even Number.

#1 Best Practices Solution by g964 (plus 24 more warriors)

def nth_even(n):
    return 2 * (n - 1);

"""


def nth_even(n):
    """get's the nth even number."""
    even_numbers = []
    m = 0
    while len(even_numbers) != n:
        even_numbers.append(m)
        m += 2
    return even_numbers[-1]