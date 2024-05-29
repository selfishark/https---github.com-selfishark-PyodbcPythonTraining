def _is_perfect_length(sequence):
    """The purpose of this function is to determine whether the length of a given sequence 
    (e.g., a string, list, or tuple) is a “perfect” length of 2n - 1.
    """
    n = len(sequence)
    return ((n+1) & n == 0) and (n != 0)


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
# >>> express_tree = ["*", "+", "-", "a", "b", "c", "d", "e"]
# >>> iterator = LevelOrderIterator(express_tree)
# >>> next(iterator) OR " ".join(iterator)
