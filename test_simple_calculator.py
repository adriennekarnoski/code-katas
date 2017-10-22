"""Test the simple calculator."""


import pytest


def test_calculator():
    """test the bucket function."""
    from simple_calculator import calculator
    test_value = calculator(6, 2, '+')
    assert test_value == 8