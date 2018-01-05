"""Fix the loop!

Your collegue wrote an simple loop to list his favourite animals.
But there seems to be a minor mistake in the grammar,
which prevents the program to work.

If you pass the list of your favourite animals to the function,
you should get the list of the animals with orderings and newlines added

#1 Best Practices Solution by Unnamed, d0486467:

def list_animals(animals):
    return ''.join('{}. {}\n'.format(i, x) for (i, x) in enumerate(animals, 1))

"""


def list_animals(animals):
    """Takes a list of animals and makes them a numbered list."""
    animal_list = []
    for idx, animal in enumerate(animals):
        animal_list.append("{}. {}\n".format(idx + 1, animal))
    return ''.join(animal_list)
