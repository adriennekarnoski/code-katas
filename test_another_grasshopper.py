"""Test the move function."""


import pytest


def test_move():
    """test the nth_even function."""
    from another_grasshopper import move
    test_value = move(3, 6)
    assert test_value == 15