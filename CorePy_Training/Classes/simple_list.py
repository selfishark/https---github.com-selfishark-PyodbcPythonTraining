class SimpleList:
    def __init__(self, items):  # Initialize the SimpleList with a list of items
        self._items = list(items)

    def add(self, item):  # Add an item to the end of the SimpleList
        self._items.append(item)

    def __getitem__(self, index):  # Get the item at a specific index in the SimpleList
        return self._items[index]

    def sort(self):  # Sort the items in the SimpleList in ascending order
        self._items.sort()

    def __len__(self):  # Get the number of items in the SimpleList
        return len(self._items)

    def __repr__(self):  # Get a string representation of the inheriting object
        return f'{type(self).__name__}({self._items!r})'    # !r converts the value using repr() before formatting it.


class SortedList(SimpleList):  # SortedList class that inherits from SimpleList
    def __init__(self, items=()):  
        super().__init__(items)  # Call the __init__ method of the parent class (SimpleList) using the super() method
        self.sort()  # Sort the items after initializing

    def add(self, item):  
        super().add(item)  # Call the add method of the parent class (SimpleList)
        self.sort()  # Sort the items after adding a new one


class IntList(SimpleList):  # IntList class that inherits from SimpleList
    def __init__(self, items=()):  
        for x in items: self._validate(x)  # Validate each item in the provided iterable
        super().__init__(items)  # Call the __init__ method of the parent class (SimpleList)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')  # Raise an error if the item is not an integer

    def add(self, item):
        self._validate(item)  # Validate the item
        super().add(item)  # Call the add method of the parent class (SimpleList)


class SortedIntList(IntList, SortedList):  # multiple inheritance class
    pass