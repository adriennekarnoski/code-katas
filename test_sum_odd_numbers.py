"""Test the sum_odd_numbers function."""


import pytest


def test_row_sum_odd_numbers():
    """Test correct return."""
    from sum_odd_numbers import row_sum_odd_numbers
    testing = row_sum_odd_numbers(19)
    assert testing == 6859