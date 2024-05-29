from operator import index
from turtle import right
from unittest import result


def _is_perfect_length(sequence):
    """The purpose of this function is to determine whether the length of a given sequence 
    (e.g., a string, list, or tuple) is a “perfect” length of 2n - 1.
    """
    n = len(sequence)
    return ((n+1) & n == 0) and (n != 0)

##############

# breath-first level order of a binary tree
# a level by level traversal of the tree
class LevelOrderIterator:

    def __init__(self, sequence):
        if not _is_perfect_length(sequence):    # checking if the length of the sequence meets the required size before proceeding
            raise ValueError(
                f"this sequence of length {len(sequence)} "
                "must be of a perfect length (2n - 1)."
            )
        self._sequence = sequence   # this sequence could be a list or any other iterable
        self._index = 0     # track the element in the sequence or internal state

    def __next__(self):     # the built-in function that traverse the sequence
        if self._index >= len(self._sequence):
            raise StopIteration     # if you reach the end of the sequence
        result = self._sequence[self._index]    # retrieve the current sequence element
        self._index += 1    # to yield the following element
        return result

    def __iter__(self):     # the iteration built-in function that allows the class to be used anywhere an iterable is required
        return self

# Usage:

# >>> from iterators import *
# >>> express_tree = ["*", "+", "-", "a", "b", "c", "d"]
# >>> iterator = LevelOrderIterator(express_tree)
# >>> next(iterator) OR " ".join(iterator)

##############

# return the index of the respective child element given the parent's index
def _left_child(index):
    return 2 * index + 1    # left child: 2n + 1

def _right_child(index):
    return 2 * index + 2    # right child: 2n + 2


# depth-first pre-order binary tree
# parent before child and left child before right child
class PreOrderIterator:

    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"this sequence of length {len(sequence)} "
                "must be of a perfect length (2n - 1)."
            )
        self._sequence = sequence
        self._stack = [0]   # track the element using a stack of indexes, starting with the root 0

    def __next__(self):
        if len(self._stack) == 0:   # if the stack is empty stop the iteration
            raise StopIteration

        index = self._stack.pop()   # otherwise, pop the top value off the stack to get the current index
        result = self._sequence[index]   # and capture the results of the current iteration into a local variable by indexing into the sequence over which we are iterating

        # NOW push the value of the left and right children onto the stack
        # starting with the right child as pre-order respect last-in-first-out
        right_child_index = _right_child(index)     # generate a candidate index for the right child over the current element
        if right_child_index < len(self._sequence):  # check if the current child lies within the bounds of the sequence, if not it is a leaf node with no right child
            self._stack.append(right_child_index)   # add the right child

        left_child_index = _right_child(index)
        if left_child_index < len(self._sequence):
            self._stack.append(left_child_index)

        return result   # the result of the current element


    def __iter__(self):
        return self

# Usage

# >>> from iterators import *
# >>> express_tree = "* + - a b c d".split() OR ["*", "+", "-", "a", "b", "c", "d"]   
# >>> iterator = PreOrderedIterator(express_tree)
# >>> " ".join(iterator)
##############


# depth-first in-order binary tree
# left subtree before current node before right node
class PreOrderIterator:

    def __init__(self, sequence):
        if not _is_perfect_length(sequence):
            raise ValueError(
                f"this sequence of length {len(sequence)} "
                "must be of a perfect length (2n - 1)."
            )
        self._sequence = sequence
        self._stack = []    # an empty stack at the start
        self._index = 0     # index 0 is the root of the tree

    def __next__(self):
        if (len(self._stack) == 0) and (self._index >= len(self._sequence)):     # Stop the iteration if the stack is empty and the index is out of bounds
            raise StopIteration

        # 
        while self._index < len(self._sequence):
            self._stack.append(self._index)
            self._index = _left_child(self._index)


##############
# Usage:

# >>> from iterators import *
# >>> express_tree = ["*", "+", "-", "a", "b", "c", "d", "e"]
# >>> iterator = LevelOrderIterator(express_tree)
# >>> next(iterator) OR " ".join(iterator)
