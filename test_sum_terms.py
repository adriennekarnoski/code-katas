"""Test the sum of terms function."""


import pytest


SUM_TABLE = [
    (1, "1.00"),
    (2, "1.25"),
    (3, "1.39"),
    (0, "0.00")
]


@pytest.mark.parametrize('n, result', SUM_TABLE)
def test_series_sum(n, result):
    """test the bucket function."""
    from sum_terms import series_sum
    assert series_sum(n) == result
