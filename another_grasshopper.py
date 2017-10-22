"""Grasshopper - Terminal game move function

Create a function for the terminal game that takes the current position of the 
hero and the roll (1-6) and return the new position.

#1 Best Practices Solution by amone (plus 24 more warriors)

def move(position, roll):
    return position + 2*roll

"""


def move(position, roll):
    """position plus double the roll amount."""
    return position + (roll * 2)