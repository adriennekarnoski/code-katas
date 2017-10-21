"""Test the sum_two_smallest_numbers function."""


import pytest


def test_sum_two_smallest_numbers():
    """Test that function is returning something other than 0."""
    from sum_of_lowest import sum_two_smallest_numbers
    test_return = sum_two_smallest_numbers([1, 2, 3])
    assert test_return != 0


SUM_TABLE = [
    ([3, 2, 27, 5, 10, 16], 5),
    ([6, 4, 8, 87, 1, 2], 3),
    ([1, 6, 9, 8, 5, 7], 6)
]

@pytest.mark.parametrize('n, result', SUM_TABLE)
def test_list_length(n, result):
    """Test that returned number is correct amount."""
    from sum_of_lowest import sum_two_smallest_numbers
    assert sum_two_smallest_numbers(n) == result