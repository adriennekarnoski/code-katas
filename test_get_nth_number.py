"""Test the sum_odd_numbers function."""


import pytest


def test_nth_even():
    """test the nth_even function."""
    from get_nth_number import nth_even
    test_value = nth_even(100)
    assert test_value == 198