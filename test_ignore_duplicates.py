"""Test the ignore_duplicates function."""


import pytest


def sum_no_duplicates(numbers):
    """Test ignore duplicate function."""
    from ignore_duplicates import sum_no_duplicates
    check_answer = sum_no_duplicates([1, 1, 2, 2, 3, 4, 5])
    assert check_answer == 12
