"""Test the sum_two_smallest_numbers function."""


import pytest


RESULT_TABLE = [
    ('25abcd26', 'y1234z'),
    ('18zyz14', 'r262526n'),
    ('a1b2c3d4', '1a2b3c4d'),
    ('5a8p17', 'e1h16q'),
    ('5a8p17o', 'e1h16q15'),
    ('25252525', 'yyyy'),
    ('yyyy', '25252525')
]


@pytest.mark.parametrize('n, result', RESULT_TABLE)
def test_lAlphaNum_NumAlpha(n, result):
    """Test that returned number is correct amount."""
    from alpha_numeric import AlphaNum_NumAlpha
    assert AlphaNum_NumAlpha(n) == result