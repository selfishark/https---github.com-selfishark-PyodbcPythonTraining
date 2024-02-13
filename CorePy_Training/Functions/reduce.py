from functools import reduce
import operator

# The 'reduce()' function is used to apply a binary function (in this case, 'operator.add') to an iterable (in this case, the list [1, 2, 3, 4, 5]) in a cumulative way.
# This means that 'reduce()' starts by applying 'operator.add' to the first two elements of the iterable, then applies 'operator.add' to the result and the next element, and so on.
# The result is a single value that is the result of the cumulative application of 'operator.add' to all elements of the iterable.
# In this case, 'reduce()' adds all numbers in the list together, one after the other, resulting in 15.

reduced = reduce(operator.add, [1, 2, 3, 4, 5])

# Print the result
print(reduced)  # 15

#### Note: 
# - reduce raise a type error if the iterable is empty
# - reduce raises a type error if the iterable has only one element; That element will be returned without calling the reducing function
