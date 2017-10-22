"""Test the damage function."""


import pytest


def test_combat():
    """test the nth_even function."""
    from grasshopper import combat
    test_value = combat(100, 5)
    assert test_value == 95