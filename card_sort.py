"""Sorts a shuffled list of cards,

so that any given list of cards is sorted by rank,

no matter the starting collection."""

from priorityq import PriorityQueue


def sort_cards(cards):
    """Function to sort cards."""
    p = PriorityQueue()
    priorities = {
        'A': 13,
        'T': 4,
        'J': 3,
        'Q': 2,
        'K': 1
    }
    for card in cards:
        if card.isdigit():
            p.insert(card, 14 - int(card))
        else:
            p.insert(card, priorities[card])
    sorted_cards = []
    while p.size is not 0:
        sorted_cards.append(p.pop())
    return sorted_cards
