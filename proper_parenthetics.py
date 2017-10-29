"""Function that takes in a string of parens and returns a value
based on whether the parens are open, balanced, or broken."""


class Node(object):
    """Build a node object."""

    def __init__(self, data=None, next=None):
        """Constructor for the Node object."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Build linked list."""

    def __init__(self, iterable=()):
        """Constructor for the Linked List object."""
        self.head = None
        self._counter = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Add a new value to the head of the Linked List."""
        new_head = Node(val, self.head)
        self.head = new_head
        self._counter += 1

    def value(self):
        """Get the value of the string input."""
        node = self.head
        value = 0
        while node and value >= 0:
            if node.data == '(':
                value += 1
                node = node.next
            elif node.data == ')':
                value -= 1
                node = node.next
        return value


def check_parens(input):
    """Function that takes in string and returns value."""
    l = LinkedList()
    for paren in input[::-1]:
        l.push(paren)
    value = l.value()
    if value >= 1:
        return 1
    else:
        return value
