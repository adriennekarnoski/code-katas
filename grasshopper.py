"""Grasshopper - Terminal game combat function

Create a combat function that takes the player's current health
and the amount of damage recieved, and returns the player's new health.
Health can't be less than 0.

#1 Best Practices Solution by ZozoFouchtra (plus 17 more warriors)

def combat(health, damage):
    return max(0, health-damage)

"""


def combat(health, damage):
    """Take health and damage and return difference or zero."""
    new_health = health - damage
    if new_health <= 0:
        return 0
    else:
        return new_health