"""Test that the loop is fixed."""


import pytest


def test_list_animals():
    """test the bucket function."""
    from fix_loop import list_animals
    test_value = list_animals(['dog', 'cat', 'elephant'])
    assert test_value == '1. dog\n2. cat\n3. elephant\n'