"""Test the sum_odd_numbers function."""


import pytest


def test_high():
    """Test the high function."""
    from highest_scoring_word import high
    test_case = high('man i need a taxi up to ubud')
    assert test_case == 'taxi'