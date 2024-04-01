""" Unit tests for the stack data structure

test_methodname... etc
"""

import pytest
from dstruct.stack import Stack

@pytest.fixture
def stack():
    s = Stack()
    s.push(3)
    s.push(4)

    return s

def test_constructor():
    s = Stack()

    assert isinstance(s, Stack), "Did not construct a stack"
    assert s.size() == 0, "Stack is not empty"
    assert len(s) == 0, "Stack is not empty"

def test_push(stack):
    assert len(stack) == 2, "Expected length 2"
    stack.push(5)
    assert len(stack) == 3, "Expected length 3"

def test_pop(stack):
    assert stack.pop() == 4, "Wrong value, expect 4"
    assert len(stack) == 1, "Wrong size, expected size = 1"

