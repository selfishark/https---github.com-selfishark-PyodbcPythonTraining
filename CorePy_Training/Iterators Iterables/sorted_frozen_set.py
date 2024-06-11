from collections.abc import Sequence


class SortedFrozenSet(Sequence):

    def __init__(self, items=None):     # None is preferred than [] to initialize an empty argument
        self._items = tuple(sorted(           # sorted allow to maintain the sorting expectation
            set(items) if (items is not None)  # store items of the initialiser _items in a 'set' list to avoid duplicates
            else set()
        ))

    def __contains__(self, item):   # use the built-in __contains__ to allow the container to be queried with 'in' and 'not in'
        return item in self._items  # Returns True if the item is in the set

    def __len__(self):              # use the built-in __len__ which will be delegated when the len() method is called
        return len(self._items)     # return the number of _items

    def __iter__(self):             # use the built-in __iter__ which will be delegated when the
        return iter(self._items)

    # # can use a generator function like 'yield' to produce iterable objects as well (optional)
    # def __iter__(self):
    #     for item in self._items:
    #         yield item

    def __getitem__(self, index):   # use the built-in __getitem__ to access the indexing property,
        result = self._items[index]  # __getitem__ also delegates to 'list', therefore its results is wrapped to avoid a slicing errors
        return (
            SortedFrozenSet(result)     # wrap the result in a SortedFrozenSet object
            if isinstance(index, slice)  # check its slice object type
            else result
        )

    def __repr__(self):
        return "{type}({arg})".format(
            type=type(self).__name__,
            arg=(
                "[{}]".format(
                    ", ".join(
                        map(repr, self._items)
                    )
                )
                if self._items else ""
            )
        )

    def __eq__(self, rhs):
        if not isinstance(rhs, type(self)):
            return NotImplemented
        return self._items == rhs._items

    def __hash__(self):
        return hash(
            (type(self), self._items)
        )
