"""Test sort cards function."""

import pytest

sorted_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']


def test_sort_cards_returns_list():
    """Test the sort card function returns a list."""
    from card_sort import sort_cards
    cards = 'AJK'
    testing = sort_cards(cards)
    assert isinstance(testing, list)


def test_sort_cards_list_returned_is_correct_length():
    """Test the returned list is the same length as cards going in."""
    from card_sort import sort_cards
    cards = 'AJK'
    testing = sort_cards(cards)
    assert len(testing) == 3


def test_card_sorting_with_code_war_test_one():
    """Running the tests from codewars."""
    from card_sort import sort_cards
    cards = '39A5T824Q7J6K'
    testing = sort_cards(cards)
    assert testing == sorted_cards


def test_card_sorting_with_code_war_test_two():
    """Running the tests from codewars."""
    from card_sort import sort_cards
    cards = 'Q286JK395A47T'
    testing = sort_cards(cards)
    assert testing == sorted_cards


def test_card_sorting_with_code_war_test_two():
    """Running the tests from codewars."""
    from card_sort import sort_cards
    cards = '54TQKJ69327A8'
    testing = sort_cards(cards)
    assert testing == sorted_cards