"""Test the check_parens function returns 1, 0, or -1."""


import pytest

VALUE_TABLE = [
    ('()()()', 0),
    ('(((()', 1),
    ('()))))', -1),
    (')()', -1),
    ('(', 1),
    ('((()))', 0)
]


@pytest.mark.parametrize('n, result', VALUE_TABLE)
def test_parens_value(n, result):
    """Test that the value returned is correct."""
    from proper_parenthetics import check_parens
    assert check_parens(n) == result
