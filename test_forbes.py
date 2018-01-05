"""Test forbes function."""

import pytest


def test_return_from_function_has_two_items():
    """Test the function returns two values, oldest and youngest."""
    from forbes import forbes_function
    forbes_return = forbes_function()
    assert len(forbes_return) == 2


def test_oldest_age_not_over_80():
    """Test the oldest person age is not 80 or over."""
    from forbes import forbes_function
    forbes_return = forbes_function()
    assert forbes_return[0]['age'] < 80


def test_oldest_person_info_included():
    """Test that all information for oldest person is there."""
    from forbes import forbes_function
    forbes_return = forbes_function()
    for item in forbes_return[0]:
        assert forbes_return[0][item] is not ''


def test_youngest_age_not_under_one():
    """Test the youngest person age is a real number."""
    from forbes import forbes_function
    forbes_return = forbes_function()
    assert forbes_return[1]['age'] > 0


def test_youngest_person_info_included():
    """Test that all information for youngest person is there."""
    from forbes import forbes_function
    forbes_return = forbes_function()
    for item in forbes_return[1]:
        assert forbes_return[1][item] is not ''