"""Test the man in west function."""


import pytest


def test_check_the_bucket():
    """test the bucket function."""
    from man_in_west import check_the_bucket
    test_value = check_the_bucket(['stone', 'stone', 'gold', 'stone'])
    assert test_value == True