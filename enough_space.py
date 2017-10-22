"""Will there be enough space?

You have to write a function that accepts three parameters:
cap is the amount of people the bus can hold excluding the driver,
on is the number of people on the bus,
and wait is the number of people waiting to get on to the bus.
If there is enough space, return 0, and if there isn't,
return the number of passengers he can't take.

#1 Best Practices Solution by vaskinyy, AlexBaier, DCoulter

def enough(cap, on, wait):
    return max(0, wait - (cap - on))

"""


def enough(cap, on, wait):
    """determines if there is spave available."""
    room_available = cap - on
    getting_on = room_available - wait
    if getting_on < 0:
        return abs(getting_on)
    else: 
        return 0