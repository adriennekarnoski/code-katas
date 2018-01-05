"""Test the move function."""


import pytest


def test_enough():
    """test the enough funstion."""
    from enough_space import enough
    test_value = enough(100, 60, 50)
    assert test_value == 10