"""
stack.py: A basic stack implementation (pop, push, etc.)
"""

class Stack:
    def __init__(self):
        self._items = []

    def push(self, x):
        """ Push an element, x, to the top of the stack """
        self._items.append(x)

    def pop(self):
        """ Removes the top element from the stack
        and returns that element """
        try:
            return self._items.pop()
        except IndexError:
            return None

    def top(self):
        """ What is the top element of the stack """
        if len(self._items) == 0:
            return None
        else:
            return self._items[-1]

    def size(self):
        """ The number of items stored in the stack """
        return len(self._items)

    def __len__(self):
        return len(self._items)

